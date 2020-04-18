class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits) - 1
        s = 0
        rs = []
        for i in range(len(digits)):
            s = s + digits[i] * (10 ** l)
            l = l - 1
        for j in str(s + 1):
            rs.append(int(j))
        return rs
