numero_inteiro = int(input("Digite um número inteiro: "))
soma_digitos = 0
while (numero_inteiro // 10) or (numero_inteiro % 10) != 0:
    digito_atual   = numero_inteiro % 10
    soma_digitos   = soma_digitos + digito_atual
    numero_inteiro = numero_inteiro // 10
print(soma_digitos)