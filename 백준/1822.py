n, m = map(int, input().split())

a = set(map(int, input().split()))
b = set(map(int, input().split()))

c = sorted(list(a - b))

if len(c) == 0:
  print(0)
else:
  print(len(c))

  for i in c:
    print(i, end=' ')
