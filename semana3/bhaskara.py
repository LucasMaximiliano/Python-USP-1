## Este programa calcula as raízes reais do polinômio ax²+bx+c.
#  Input:
a = float(input("Insira o coeficiente de 2º grau: "))
b = float(input("Insira o coeficiente de 1º grau: "))
c = float(input("Insira a constante independente: "))
# Processamento de dados:
from math import sqrt
delta = b**2 - 4*a*c
if delta==0:
    r = -b/2*a
    print("A única solução é", r)
else:
    if delta>0:
        r1 = (-b + sqrt(delta)) / (2*a)
        r2 = (-b - sqrt(delta)) / (2*a)
        print("As raízes são:", r1, "e", r2)
    else:
        print("Não existem raízes reais.")
