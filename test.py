'''
test file for solution
'''
from LetterCombinationsofaPhoneNumber import *

def test_func(INPUT, OUTPUT):
    assert letterCombinations(INPUT) == OUTPUT, "Dont cool"

if __name__ == '__main__':
    test_func("23", ["ad","ae","af","bd","be","bf","cd","ce","cf"])
