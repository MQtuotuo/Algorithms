class Solution:
    def reverse(self, x: int) -> int:

        x = list(str(x))
        flag = False
        if x[0] == '-':
            flag = True
            x = x[1:]
        mid = int(len(x) / 2)
        for i in range(mid):
            tmp = x[i]
            x[i] = x[len(x) - 1 - i]
            x[len(x) - 1 - i] = tmp
        if flag:
            rs = -1 * int(''.join(x))
        else:
            rs = 1 * int(''.join(x))
        if rs > 2 ** 31 - 1 or rs < (-2) ** 31:
            return 0
        else:
            return rs