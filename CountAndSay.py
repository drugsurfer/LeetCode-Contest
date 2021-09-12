'''
To determine how you "say" a digit string, split it into the minimal number of groups so that each group is a contiguous section all of the same character.
 Then for each group, say the number of characters, then say the character.
 To convert the saying into a digit string, replace the counts with a number and concatenate every saying.
'''
def countAndSay(n):
    result = ""
    if n == 1:
        return "1"
    else:
        count = 1
        s = countAndSay(n - 1)
        for i in range(len(s)):
            if i == len(s) - 1 or s[i] != s[i + 1]:
                result += str(count) + s[i]
                count = 1
            else:
                count += 1
    return result

