n = int(input())
p = list(map(int, input().split()))

p.sort()

print(sum(sum(p[:i + 1]) for i in range(n)))
