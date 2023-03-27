numero_inteiro = int(input("Digite um número inteiro cuja soma dos digitos será calculada: "))
soma_digitos = 0
while (numero_inteiro // 10) or (numero_inteiro % 10) != 0: # Ambos os casos 1 e 10 considerados (por ex.)
    digito_atual   = numero_inteiro % 10
    soma_digitos   = soma_digitos + digito_atual
    numero_inteiro = numero_inteiro // 10
print("A soma dos digitos é:", soma_digitos)