def titleToNumber( s: str) -> int:
    res = 0
    for i in s:
        res = res * 26 + ord(i) - 64  # 64 = ord('A') - 1
    return res

print(titleToNumber('BZ'))