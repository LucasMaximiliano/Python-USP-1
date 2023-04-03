def primalidade(n):
    i = n-1
    primo = True
    while i > 1:
        if n % i == 0:
            primo = False
            break
        i -= 1
    return primo

def maior_primo(n):
    i = n
    while i >= 2:
        if(primalidade(i)):
            maiorPrimo = i
            break
        else:
            i -= 1        
    return maiorPrimo

# Testes:
def test_maior_primo100():
    assert maior_primo(100) == 97

def test_maior_primo7():
    assert maior_primo(7) == 7

def test_maior_primo2():
    assert maior_primo(2) == 2