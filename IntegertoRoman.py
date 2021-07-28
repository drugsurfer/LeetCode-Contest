'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
'''
def intToRoman(num : int) -> str:
    abc = {
        "I" : 1,
        "IV" : 4,
        "V" : 5,
        "IX" : 9,
        "X" : 10,
        "XL" : 40,
        "L" : 50,
        "XC" : 90,
        "C" : 100,
        "CD" : 400,
        "D" : 500,
        "CM" : 900,
        "M" : 1000
    }
    result = []
    for sym, number in reversed(abc.items()):
        while num > 0:
            if number <= num:
                result.append(sym)
                num -= number
            else:
                break
    return "".join(result)
