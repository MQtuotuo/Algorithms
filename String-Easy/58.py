class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        flag = False
        if len(s) == 0:
            return 0
        for i in range(len(s)):
            if s[len(s) - i - 1] != ' ':
                length += 1
            elif s[len(s) - i - 1] == ' ' and length > 0:
                return length

        return length

