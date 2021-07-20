'''
Given a string s, find the length of the longest substring without repeating characters.
'''
def lengthOfLongestSubstring(s):
    start, result = 0, 0
    for i, sym in enumerate(s):
        if sym not in s[start : i]:
            continue
        else:
            result = max(result, i - start)
            for s_ in s[start : i]:
                start += 1
                if s_ == sym:
                    break
    return max(result, len(s) - start)

