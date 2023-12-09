m, n = map(int, input().split())

lst = list(range(n + 1))

for i in range(2, int(n**0.5) + 1):
    if lst[i]:
        for j in range(i + i, n + 1, i):
            lst[j] = 0

for i in range(max(2, m), n + 1):
    if lst[i]:
        print(i)
