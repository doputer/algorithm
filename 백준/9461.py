p = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0] * 90

for i in range(10, 100):
    p[i] = p[i - 2] + p[i - 3]

t = int(input())

for _ in range(t):
    n = int(input())
    print(p[n - 1])
