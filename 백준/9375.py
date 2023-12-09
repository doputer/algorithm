t = int(input())

for _ in range(t):
    n = int(input())
    wears = {}

    for _ in range(n):
        _, wear_type = input().split(" ")

        if wear_type in wears:
            wears[wear_type] += 1
        else:
            wears[wear_type] = 1

    i = 1

    for v in wears.values():
        i *= v + 1

    print(i - 1)
