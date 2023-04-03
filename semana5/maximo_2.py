def maximo(a, b):
    if a >= b:
        return a
    else:
        return b
    
def test_maximo_pos():
    assert maximo(1,2) == 2

def test_maximo_igual():
    assert maximo(1,1) == 1

def test_maximo_neg():
    assert maximo(-1,-2) == -1

def test_maximo_misturado():
    assert maximo(1,-2) == 1