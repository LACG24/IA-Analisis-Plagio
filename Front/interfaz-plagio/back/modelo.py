import os
import re
import torch
import pandas as pd
import numpy as np
from transformers import RobertaTokenizer, RobertaModel
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from difflib import SequenceMatcher
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from scipy.spatial.distance import euclidean

# === Inicializar CodeBERT ===
vectorizer = TfidfVectorizer(ngram_range=(1, 3), analyzer='word')
tokenizer = RobertaTokenizer.from_pretrained("microsoft/codebert-base")
model = RobertaModel.from_pretrained("microsoft/codebert-base", output_hidden_states=True)

def get_embedding(text, capa=4):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    hidden_states = outputs.hidden_states  # Lista de 13 tensores (incluye embedding inicial)
    capa_oculta = hidden_states[capa]      # Selecciona la capa que quieras

    # Tomamos el vector del token [CLS] de esa capa
    return capa_oculta[:, 0, :].squeeze().numpy()

# === Función para anonimizar código ===
def anonimizar_codigo(code):
    tokens = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', code)
    usados = {}
    nuevo_codigo = code
    contador = 1
    for tok in tokens:
        if tok not in usados and tok not in {"def", "if", "else", "for", "while", "return", "print", "input"}:
            usados[tok] = f"VAR_{contador}"
            contador += 1
    for original, nuevo in usados.items():
        nuevo_codigo = re.sub(rf'\b{original}\b', nuevo, nuevo_codigo)
    return nuevo_codigo

# === Extraer todas las funciones de un archivo ===
def extraer_todas_funciones(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        code = f.read()
    funciones = re.findall(r"(def\s+[a-zA-Z_][a-zA-Z0-9_]*\(.*?\):(?:\n(?:\s{4}|\t).*)*)", code)
    return funciones if funciones else [code]

def ratio_similitud_bruta(c1, c2):
    return SequenceMatcher(None, c1, c2).ratio()

def contar_identificadores(cod1, cod2):
    tokens1 = set(re.findall(r'\b[a-zA-Z_]\w*\b', cod1))
    tokens2 = set(re.findall(r'\b[a-zA-Z_]\w*\b', cod2))
    comunes = tokens1 & tokens2
    dif = (tokens1 | tokens2) - comunes
    return len(dif)

def lineas_iguales(c1, c2):
    l1 = set(c1.splitlines())
    l2 = set(c2.splitlines())
    return len(l1 & l2)

def features_por_par(path1, path2):
    if not os.path.exists(path1) or not os.path.exists(path2):
        return None

    funcs1 = extraer_todas_funciones(path1)
    funcs2 = extraer_todas_funciones(path2)

    # Anonimizamos funciones
    funcs1_anon = [anonimizar_codigo(f) for f in funcs1]
    funcs2_anon = [anonimizar_codigo(f) for f in funcs2]

    # Embeddings con CodeBERT (por función)
    emb1 = [get_embedding(f, capa=4) for f in funcs1_anon]
    emb2 = [get_embedding(f, capa=4) for f in funcs2_anon]

    if not emb1 or not emb2:
        return None

    # Distancias Euclidianas negativas entre todas las combinaciones
    distancias = [-euclidean(e1, e2) for e1 in emb1 for e2 in emb2]

    max_sim = max(distancias)
    avg_sim = np.mean(distancias)
    count_95 = sum(1 for s in distancias if s > -0.05)
    count_90 = sum(1 for s in distancias if s > -0.1)

    # Texto original y anonimizado completo
    all_code1 = " ".join(funcs1_anon)
    all_code2 = " ".join(funcs2_anon)
    raw_code1 = " ".join(funcs1)
    raw_code2 = " ".join(funcs2)

    # TF-IDF similarity (cosine)
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([all_code1, all_code2])
    sim_tfidf = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]

    # Métricas adicionales
    sim_bruta = ratio_similitud_bruta(raw_code1, raw_code2)
    idf_diff = contar_identificadores(raw_code1, raw_code2)
    lineas_eq = lineas_iguales(raw_code1, raw_code2)

    return [
        max_sim, avg_sim, count_95, count_90,
        len(emb1), len(emb2), sim_tfidf,
        sim_bruta, idf_diff, lineas_eq
    ]