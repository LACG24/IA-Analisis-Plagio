import math, sys

sys.setrecursionlimit(10**7)
INFINITO = 10**20
EPSILON = 1e-13
MODULO = 10**9 + 7

direcciones = [(-1,0),(0,1),(1,0),(0,-1)]
diag_direcciones = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def leer_lista_enteros(): return list(map(int, sys.stdin.readline().split()))
def leer_lista_enteros_cero(): return [int(x)-1 for x in sys.stdin.readline().split()]
def leer_lista_flotantes(): return list(map(float, sys.stdin.readline().split()))
def leer_texto(): return input()
def leer_entero(): return int(sys.stdin.readline())

def distancia_euclidiana(x1, y1, x2, y2):
    return math.hypot(x1 - x2, y1 - y2)

def punto_interseccion(p1, p2, q1, q2):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = q1
    x4, y4 = q2

    a = (y4 - y3) * (x4 - x1) - (x4 - x3) * (y4 - y1)
    b = (x2 - x1) * (y4 - y1) - (y2 - y1) * (x4 - x1)
    c = (x2 - x1) * (y4 - y3) - (y2 - y1) * (x4 - x3)

    if c == 0:
        return None

    s = a / c
    t = b / c

    if 0 <= s <= 1 and 0 <= t <= 1:
        return (x1 + s * (x2 - x1), y1 + s * (y2 - y1))
    return None

def centro_circunferencia(p1, p2, p3):
    mid1 = [(p1[0]+p2[0])/2, (p1[1]+p2[1])/2]
    vec1 = [mid1[1] - p1[1], p1[0] - mid1[0]]
    mid2 = [(p1[0]+p3[0])/2, (p1[1]+p3[1])/2]
    vec2 = [mid2[1] - p1[1], p1[0] - mid2[0]]

    ext1 = [mid1[0] + vec1[0]*1e7, mid1[1] + vec1[1]*1e7]
    ext2 = [mid1[0] - vec1[0]*1e7, mid1[1] - vec1[1]*1e7]
    ext3 = [mid2[0] + vec2[0]*1e7, mid2[1] + vec2[1]*1e7]
    ext4 = [mid2[0] - vec2[0]*1e7, mid2[1] - vec2[1]*1e7]

    return punto_interseccion(ext1, ext2, ext3, ext4)

def resolver():
    casos = leer_entero()
    resultados = []
    for _ in range(casos):
        x1, y1, x2, y2, x3, y3 = leer_lista_flotantes()
        A = [x1, y1]
        B = [x2, y2]
        C = [x3, y3]
        centro = centro_circunferencia(A, B, C)
        r = distancia_euclidiana(centro[0], centro[1], x1, y1)
        resultados.append("{:.3f} {:.3f} {:.3f}".format(centro[0], centro[1], r))

    return '\n'.join(resultados)

print(resolver())
