class Solution:
    def isHappy(self, n: int) -> bool:
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




