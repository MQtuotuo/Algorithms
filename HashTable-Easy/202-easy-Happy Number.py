from typing import List


class Solution:
    def isHappy(self, n: int) -> bool:
        """
        A happy number is a number defined by the following process:

        Starting with any positive integer, replace the number by the sum of the squares of its digits.
        Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
        Those numbers for which this process ends in 1 are happy.
        Return true if n is a happy number, and false if not.

        Example 1:
        Input: n = 19
        Output: true

        Example 2:
        Input: n = 2
        Output: false

        """
        dict = {'0': 0, '1': 1, '2': 4, '3': 9, '4': 16, '5': 25, '6': 36, '7': 49, '8': 64, '9': 81}
        sum_set = set()
        res = sum([dict[x] for x in str(n)])
        if res == 1: return True
        while res != 1:
            if res in sum_set:
                return False
            else:
                sum_set.add(res)
                res = sum([dict[x] for x in str(res)])
                if res == 1: return True

print(Solution().isHappy(19))



