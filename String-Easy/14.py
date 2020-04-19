strs=["aca","cba"]
prefix = strs[0]
num = 0
for i in range(1, len(strs)):
    for j in range(min(len(strs[i]), len(prefix))):
        if prefix[num]  != strs[i][j]:
            break
        else:
            num +=1
    prefix =  ''.join(prefix[:num])
    num=0
print( prefix)


def longestCommonPrefix( S: [str]) -> str:
    if not S: return ''
    m, M, i = min(S), max(S), 0
    for i in range(min(len(m), len(M))):
        if m[i] != M[i]: break
    else:
        i += 1
    return m[:i]

s = longestCommonPrefix(strs)


def solve(eq, var):
    eq1 = eq.replace("=", "-(") + ")"
    c = eval(eq1, {var: 1j})
    return -c.real / c.imag

print(solve())