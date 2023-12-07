def dp(n):
    if n == 1:
        return 0

    happy = 0

    if n % 2 == 0:
        a, b = n // 2, n // 2
    else:
        a, b = n // 2 + 1, n // 2

    happy += a * b
    happy += dp(a)
    happy += dp(b)

    return happy


n = int(input())

print(dp(n))
