'''
Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''

def strStr(self, haystack, needle):
    if needle == "":
        return 0
    resultIndex = haystack.find(needle, 0, len(haystack))
    return resultIndex
