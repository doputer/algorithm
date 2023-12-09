n = int(input())

a, b = 1, 1
mod = int(1e9) + 7

for _ in range(n - 2):
    b, a = (a + b) % mod, b

code1 = b
code2 = n - 2

print(code1, code2)
