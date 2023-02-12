n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []

i, j = 0, 0

while i < len(a) and j < len(b):
  if a[i] < b[j]:
    c.append(a[i])
    i += 1
  else:
    c.append(b[j])
    j += 1

c += a[i:]
c += b[j:]

print(*c)
