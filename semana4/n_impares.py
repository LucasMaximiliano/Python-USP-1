n = int(input("Digite o valor de n: "))
terminou = False
i = 1
count = 0
while not terminou:
    if i % 2 != 0:
        print(i)
        count += 1
    if count == n:
        terminou = True
    i += 1
