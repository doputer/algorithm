n = int(input())

a, b = 1, 1

for _ in range(n - 1):
    a, b = (a + b + b) % 10007, a

print(a)
