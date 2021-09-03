'''
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
Return the quotient after dividing dividend by divisor.
'''
def divide(dividend, divisor):
    result = dividend / divisor
    if -2 ** 31 <= result <= 2 ** 31 - 1:
        return int(result)
    elif result > 2 ** 31 - 1:
        return 2 ** 31 - 1
    else:
        return -2 ** 31
