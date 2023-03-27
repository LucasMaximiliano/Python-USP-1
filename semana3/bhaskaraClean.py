## Este programa calcula as raízes reais do polinômio ax²+bx+c.
#  Input:
a = float(input())
b = float(input())
c = float(input())
# Processamento de dados:
from math import sqrt
delta = b**2 - 4*a*c
if delta==0:
    r = -b/2*a
    print("a raiz dupla desta equação é", r)
else:
    if delta>0:
        r1 = (-b - sqrt(delta)) / (2*a)
        r2 = (-b + sqrt(delta)) / (2*a)
        print("as raízes da equação são", r1, "e", r2)
    else:
        print("esta equação não possui raízes reais")
