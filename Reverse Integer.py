'''
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
'''
def reverse(x):
    if x == 0:
        return 0
    num = ''
    flag = True
    if x < 0:
        flag = False
        x *= -1
    while x > 0:
        num += str(x % 10)
        x //= 10
    if flag:
        num = int(num)
    else:
        num = -1 * int(num)
    if num <= 2 ** 31 - 1 and num >= -2 ** 31:
        return num
    else:
        return 0