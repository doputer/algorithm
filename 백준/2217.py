n = int(input())
ropes = [int(input()) for _ in range(n)]

ropes.sort()

print(max([ropes[i] * (n - i) for i in range(n)]))
