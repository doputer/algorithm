n, m = map(int, input().split())
card = []
max = -1
for _ in range(n):
  row = list(map(int, input().split()))
  if max < min(row):
    max = min(row)


print(max)
