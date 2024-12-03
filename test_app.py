from app import *

def test_soma():
    assert soma(2, 3) == 5

def test_multiplicacao():
    # arrange
    numero1 = 2
    numero2 = 3
    # act
    resultado = multiplicacao(numero1, numero2)
    # assert
    assert resultado == 6
