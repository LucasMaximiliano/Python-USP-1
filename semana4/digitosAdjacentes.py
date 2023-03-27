numero_inteiro = int(input("Digite um número inteiro: "))
digito_anterior = numero_inteiro % 10   # primeiro digito
numero_inteiro = numero_inteiro // 10
flag = False
while (numero_inteiro % 10) or (numero_inteiro // 10) != 0:
    digito_atual = numero_inteiro % 10
    if digito_atual == digito_anterior:
        flag = True
    # Avançar uma casa para direita:
    digito_anterior = digito_atual
    numero_inteiro  = numero_inteiro // 10
if flag:
    print("O número contêm 2 digitos adjacentes iguais.")
else:
    print("O número *não* contêm 2 digitos adjacentes iguais.")