'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''
def isValid(s):
    stack = []
    if len(s) % 2 != 0:
        return False
    opening = set('([{')
    open_close = set([('(', ')'), ('[', ']'), ('{', '}')])
    for sym in s:
        if sym in opening:
            stack.append(sym)
        else:
            if len(stack) == 0:
                return False
            L = stack.pop()
            if (L, sym) not in open_close:
                return False
    return len(stack) == 0

print(isValid("{[]}"))