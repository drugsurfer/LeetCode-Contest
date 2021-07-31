'''
Given a string containing digits from inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.2-9
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
'''
def letterCombinations(digits : str):
    numbers = {
        "2" : ['a', 'b', 'c'],
        "3": ['d', 'e', 'f'],
        "4": ['g', 'h', 'i'],
        "5": ['j', 'k', 'l'],
        "6": ['m', 'n', 'o'],
        "7": ['p', 'q', 'r', 's'],
        "8": ['t', 'u', 'v'],
        "9": ['w', 'x', 'y', 'z'],
    }
    result = []
    def back(i, curStr):
        if len(curStr) == len(digits):
            result.append(curStr)
            return
        for sym in numbers[digits[i]]:
            back(i + 1, curStr + sym)
    if digits:
        back(0, "")
    return result
