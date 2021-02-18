from exercices.exercice1 import *

def test_convertir():
    assert convertir([1, 0, 1, 0, 0, 1, 1]) == 83
    assert convertir([1, 0, 0, 0, 0, 0, 1, 0]) == 130
