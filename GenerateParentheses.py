'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''
def generateParentheses(n : int):
    stack = []
    result = []
    def backtrack(openCnt, closeCnt):
        if openCnt == closeCnt == n:
            result.append("".join(stack))
            return
        if openCnt < n:
            stack.append("(")
            backtrack(openCnt + 1, closeCnt)
            stack.pop()
        if closeCnt < openCnt:
            stack.append(")")
            backtrack(openCnt, closeCnt + 1)
            stack.pop()
    backtrack(0, 0)
    return result

if __name__ == "__main__":
    print(generateParentheses(3))