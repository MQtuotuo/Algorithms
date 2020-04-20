class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s = list(s)
        l, r = 0, len(s) - 1
        while (l <= r):
            if s[l] in vowels and s[r] in vowels:
                tmp = s[l]
                s[l] = s[r]
                s[r] = tmp
                l += 1
                r -= 1
            elif s[l] in vowels and s[r] not in vowels:
                r -= 1
            elif s[l] not in vowels and s[r] in vowels:
                l += 1
            else:
                l += 1
                r -= 1
        return ''.join(s)
