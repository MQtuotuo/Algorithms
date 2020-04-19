def addBinary( a: str, b: str) -> str:
    a = int(a, 2)
    b = int(b, 2)

    while True:
        xor_bitsum = a ^ b  # XOR gate for sum result
        and_carry = (a & b) << 1  # AND gate with a bit shift because the carry goes in the next column
        a = xor_bitsum
        b = and_carry
        if and_carry == 0:
            break

    return str(bin(a)[2:])  # start at 2 because python returns "0b" for bit wise

a='11'
b='1'
print(addBinary(a, b))