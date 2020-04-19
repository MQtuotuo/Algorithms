class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        n = len(needle)
        i = 0
        while i < len(haystack) - n + 1:
            if haystack[i:i + n] == needle:
                return i
            else:
                i = i + 1
        return -1
