'''
test file for solution
'''
from FourSum import *

def test_func(INPUT, OUTPUT):
    pass

def test_func2(INPUT, TARGET, OUTPUT):
    assert fourSum(INPUT, TARGET) == OUTPUT, "Dont cool"

if __name__ == '__main__':
    test_func2([1,0,-1,0,-2,2], 0, [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]])
    test_func2([2,2,2,2,2], 8, [[2,2,2,2]])
