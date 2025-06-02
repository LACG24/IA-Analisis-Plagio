import torch
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.utils import class_weight
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import torch.nn as nn
from modelo import features_por_par

class PlagioNet(nn.Module):
    def __init__(self, input_size, num_classes):
        super(PlagioNet, self).__init__()
        # self.net = nn.Sequential(
        #     nn.Linear(input_size, 64),
        #     nn.ReLU(),  # Más simple que ELU
        #     nn.Linear(64, 32),
        #     nn.ReLU(),
        #     nn.Linear(32, num_classes)
        # )
        # self.net = nn.Sequential(
        #     nn.Linear(input_size, 64),
        #     nn.ELU(),
        #     nn.BatchNorm1d(64),

        #     nn.Linear(64, 32),
        #     nn.ELU(),
        #     nn.BatchNorm1d(32),
        #     nn.Dropout(0.3),

        #     nn.Linear(32, num_classes)
        # )

        self.net = nn.Sequential(
            nn.Linear(input_size, 256),
            nn.ELU(),
            nn.BatchNorm1d(256),
            nn.Dropout(0.3),

            nn.Linear(256, 128),
            nn.ELU(),
            nn.BatchNorm1d(128),
            nn.Dropout(0.3),

            nn.Linear(128, 64),
            nn.ELU(),
            nn.BatchNorm1d(64),
            nn.Dropout(0.2),

            nn.Linear(64, 32),
            nn.ELU(),
            nn.Linear(32, num_classes)
        )

    def forward(self, x):
        return self.net(x)

def cargar_modelo_y_encoder(path="model.pth"):
    checkpoint = torch.load(path, map_location='cpu')

    model = PlagioNet(input_size=checkpoint['input_size'], num_classes=checkpoint['num_classes'])
    model.load_state_dict(checkpoint['model_state_dict'])
    model.eval()

    le = LabelEncoder()
    le.classes_ = np.array(checkpoint['label_encoder'])

    return model, le

model, label_encoder = cargar_modelo_y_encoder()


def predecir_par(path1, path2):
    feats = features_por_par(path1, path2)
    if feats is None:
        return "No se pudo procesar el par"

    x = torch.tensor(feats, dtype=torch.float32).unsqueeze(0)
    with torch.no_grad():
        outputs = model(x)
        probs = torch.softmax(outputs, dim=1).numpy()[0]

    resultado = []
    for idx, prob in enumerate(probs):
        tipo = label_encoder.inverse_transform([idx])[0]
        resultado.append(f"Tipo {tipo}: {prob*100:.2f}%")

    return "\\n".join(resultado)