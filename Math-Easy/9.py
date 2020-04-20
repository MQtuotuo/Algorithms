class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        reverse = str(x)[::-1]
        if x==int(reverse):
            return True
        else:
            return False