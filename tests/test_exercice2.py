from exercices.exercice2 import *

def test_tri_insertion():
    assert tri_insertion([2, 5, -1, 7, 0, 28]) == [-1, 0, 2, 5, 7, 28]
    assert tri_insertion([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
