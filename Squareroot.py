def square_root(n):
    if n == 0:
        return 0
    left, right = 1, n
    res = -1
    while left <= right:
        mid = (left + right) // 2
        if mid * mid <= n:
            res = mid
            left = mid + 1
        else:
            right = mid - 1
    return res

## Driver code
print("Square root:", square_root(4))
print("Square root:", square_root(8))
print("Square root:", square_root(10))