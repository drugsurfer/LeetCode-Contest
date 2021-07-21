'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
'''
def convert(s, numRows):
    if numRows == 1: return s
    text = [''] * numRows
    flag = True
    i, j = 0, 0
    count = 0
    while i < len(s):
        count += 1
        if count == numRows:
            count = 1
            flag = not flag
        if flag:
            text[j] += s[i]
            j += 1
        elif not flag:
            text[j] += s[i]
            j -= 1
        i += 1
    result = ''
    for i in text:
        result += i
    return result



