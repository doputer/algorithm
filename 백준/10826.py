n = int(input())

a, b = 0, 1

for _ in range(n):
    b, a = a + b, b

print(a)
