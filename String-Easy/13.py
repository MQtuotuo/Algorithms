class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        s_list = [char for char in s]
        if len(s_list) == 1:
            return m[s_list[0]]
        i = 0
        rs = 0

        while i < len(s_list) - 1:

            if (s_list[i] == 'I' and s_list[i + 1] == 'V') or (s_list[i] == 'I' and s_list[i + 1] == 'X'):
                rs = rs + m[s_list[i + 1]] - m[s_list[i]]
                i = i + 2

            elif (s_list[i] == 'X' and s_list[i + 1] == 'L') or (s_list[i] == 'X' and s_list[i + 1] == 'C'):
                rs = rs + m[s_list[i + 1]] - m[s_list[i]]
                i = i + 2

            elif (s_list[i] == 'C' and s_list[i + 1] == 'D') or (s_list[i] == 'C' and s_list[i + 1] == 'M'):
                rs = rs + m[s_list[i + 1]] - m[s_list[i]]
                i = i + 2
            else:
                rs = rs + m[s_list[i]]
                i = i + 1

        if m[s_list[-1]] <= m[s_list[-2]]:
            rs += m[s_list[-1]]
        return rs


