def fizzbuzz(n):
    if n%3 == 0:
        if n%5 == 0:
            return "FizzBuzz"
        else:
            return "Fizz"
    else:
        if n%5 == 0:
            return "Buzz"
        else:
            return n
        
# Testes:
def test_fizz():
    assert fizzbuzz(3) == "Fizz"

def test_buzz():
    assert fizzbuzz(5) == "Buzz"

def test_fizzbuzz():
    assert fizzbuzz(15) == "FizzBuzz"

def test_fail():
    assert fizzbuzz(4) == 4