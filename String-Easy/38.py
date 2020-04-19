def calc(s: str):
    i = 0
    j=0
    count = 0
    rs = []
    while i < len(s):

        if s[i] == s[j]:
            count += 1
            i += 1
        else:
            rs.append(str(count))
            rs.append(s[i-1])
            j+=count
            count = 0
    rs.append(str(count))
    rs.append(s[i - 1])
    return ''.join(rs)


def countAndSay(n: int) -> str:
    if n == 1:
        return '1'
    else:
        init = calc('1')
        for i in range(0, n-2):
            init = calc(init)

    return init


print(calc('1211'))

