class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)
        mid = int(length / 2)

        for i in range(mid):
            tmp = s[i]
            s[i] = s[length - i - 1]
            s[length - i - 1] = tmp