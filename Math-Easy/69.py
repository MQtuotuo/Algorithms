def mySqrt( x: int) -> int:
    lower, upper = 0, x
    while (lower <= upper):
        mid = (lower + upper) // 2
        square = mid ** 2
        if (square == x):
            return mid
        if (square < x):
            lower = mid + 1
        else:
            upper = mid - 1
    return upper

print(mySqrt(8))