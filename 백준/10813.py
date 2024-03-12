n, m = map(int, input().split())

basket = [i + 1 for i in range(n)]

for _ in range(m):
    i, j = map(lambda x: int(x) - 1, input().split())

    basket[i], basket[j] = basket[j], basket[i]

print(*basket)
