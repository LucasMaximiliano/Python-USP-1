def fatorial(n):
    fatorial = 1
    while n != 0:
        fatorial = fatorial * n
        n -= 1
    return fatorial

def coef_binomial(n, k):
    return fatorial(n) / (fatorial(k) * fatorial(n-k))

n = int(input("Insira o valor de n: "))
k = int(input("Insira o valor de k: "))
print("n sobre k a k é igual a", coef_binomial(n, k))