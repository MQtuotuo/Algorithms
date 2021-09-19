from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        i = len(digits) - 1
        while i >= 0:
            if digits[i] + 1 != 10:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
            i -= 1
        return digits

        # l = len(digits) - 1
        # s = 0
        # rs = []
        # for i in range(len(digits)):
        #     s = s + digits[i] * (10 ** l)
        #     l = l - 1
        # for j in str(s + 1):
        #     rs.append(int(j))
        # return rs
ep = [9, 9, 9]
s = Solution()
rs = s.plusOne(ep)
print(rs)