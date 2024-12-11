import requests
import facto

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 4
    #je suppose que 3 est == a 4
    
def test_factorielle():
    assert facto.factorielle(0) == 1