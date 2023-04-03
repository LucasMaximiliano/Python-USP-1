## Este programa calcula as raízes reais do polinômio ax²+bx+c.
# Funções:
def calc_delta(a, b, c):
    return b**2 - 4*a*c
def calc_raiz_unica(a, b):
    return -b/2*a
def calc_raiz_maior(a, b, delta):
    return (-b + sqrt(delta)) / (2*a)
def calc_raiz_menor(a, b, delta):
    return (-b - sqrt(delta)) / (2*a)
#  Input:
a = float(input("Insira o coeficiente de 2º grau: "))
b = float(input("Insira o coeficiente de 1º grau: "))
c = float(input("Insira a constante independente: "))
# Processamento de dados:
from math import sqrt
delta = calc_delta(a, b, c)
if delta==0:
    r = calc_raiz_unica(a, b)
    print("A única solução é", r)
else:
    if delta>0:
        r1 = calc_raiz_maior(a, b, delta)
        r2 = calc_raiz_menor(a, b, delta)
        print("As raízes são:", r1, "e", r2)
    else:
        print("Não existem raízes reais.")
