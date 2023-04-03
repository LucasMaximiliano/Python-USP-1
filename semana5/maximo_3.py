def maximo(a, b, c):
    if a >= b:
        if a >= c:
            return a
        else:
            return c
    else:
        if b >= c:
            return b
        else:
            return c
        
# Testes:
def test_maximo1():
    assert maximo(1,2,3) == 3

def test_maximo2():
    assert maximo(1,3,2) == 3

def test_maximo3():
    assert maximo(2,1,3) == 3

def test_maximo4():
    assert maximo(2,3,1) == 3

def test_maximo5():
    assert maximo(3,1,2) == 3

def test_maximo6():
    assert maximo(3,2,1) == 3

def test_maximo7():
    assert maximo(30,14,10) == 30

def test_maximo8():
    assert maximo(0,-1,1) == 1

def test_maximo9():
    assert maximo(0,0,0) == 0

def test_maximo10():
    assert maximo(1,1,0) == 1

def test_maximo11():
    assert maximo(1,1,3) == 3