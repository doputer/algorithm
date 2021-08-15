n, m, k = map(int, input().split())
list = list(map(int, input().split()))
list.sort()

first = list[-1]
second = list[-2]


result = (first * k + second) * (m // (k + 1)) + first * (m % (k + 1))

print(result)
