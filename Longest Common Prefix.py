'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
'''
def longestCommonPrefix(strs):
    if len(strs) == 1:
        return strs[0]
    s = strs[0]
    result = ''
    flag = True
    for i in range(len(strs[0]) + 1):
        for j in range(len(strs)):
            if strs[j].startswith(strs[0][0:i]):
                flag = True
            else:
                flag = False
                break
        if flag:
            result = strs[0][0:i]
        else:
            break
    return result

