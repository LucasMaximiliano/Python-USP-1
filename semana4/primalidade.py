n = int(input("Digite um número inteiro: "))
i = n-1
primo = True
while i > 1:
    if n % i == 0:
        primo = False
        break
    i -= 1
if primo:
    print("primo")
else:
    print("não primo")