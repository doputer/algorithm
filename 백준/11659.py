import sys

n, m = map(int, sys.stdin.readline().split())

numbers = list(map(int, sys.stdin.readline().split()))
acc = [0] * (n + 1)

for i in range(1, n + 1):
  acc[i] = numbers[i - 1] + acc[i - 1]

for _ in range(m):
  i, j = map(int, sys.stdin.readline().split())

  print(acc[j] - acc[i-1])
