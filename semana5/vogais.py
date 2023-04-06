def vogal(char):
    if char == 'a' or char == 'A':
        return True
    else:
        if char == 'e' or char == 'E':
            return True
        else:
            if char == 'i' or char == 'I':
                return True
            else:
                if char == 'o' or char == 'O':
                    return True
                else:
                    if char == 'u' or char == 'U':
                        return True
                    else:
                        return False

# Testes:
def test_vogal_a():
    assert vogal("a") == True

def test_vogal_A():
    assert vogal("A") == True

def test_vogal_e():
    assert vogal("e") == True

def test_vogal_E():
    assert vogal("E") == True

def test_vogal_i():
    assert vogal("i") == True

def test_vogal_I():
    assert vogal("I") == True

def test_vogal_o():
    assert vogal("o") == True

def test_vogal_O():
    assert vogal("O") == True

def test_vogal_u():
    assert vogal("u") == True

def test_vogal_U():
    assert vogal("U") == True

def test_vogal_b():
    assert vogal("b") == False

def test_vogal_B():
    assert vogal("B") == False
