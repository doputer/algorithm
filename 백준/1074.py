def z(r, c, n, start):
    if n == 1:
        if r == 1 and c == 1:
            print(start + 3)
        elif r == 1:
            print(start + 2)
        elif c == 1:
            print(start + 1)
        else:
            print(start)

        return

    x = c < (2**n) // 2
    y = r < (2**n) // 2

    if x and y:
        z(r, c, n - 1, start)
    elif not x and y:
        z(r, c - 2 ** (n - 1), n - 1, start + (2 ** (n - 1)) ** 2)
    elif x and not y:
        z(r - 2 ** (n - 1), c, n - 1, start + 2 * (2 ** (n - 1)) ** 2)
    else:
        z(r - 2 ** (n - 1), c - 2 ** (n - 1), n - 1, start + 3 * (2 ** (n - 1)) ** 2)


n, r, c = map(int, input().split())

z(r, c, n, 0)
