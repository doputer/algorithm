def check(m, lanterns, n):
  return sum(lantern // m for lantern in lanterns) >= n


k, n = map(int, input().split())

lanterns = []

for _ in range(k):
  lanterns.append(int(input()))

l, h = 0, 2 ** 31

while l + 1 < h:
  m = (l + h) // 2

  if check(m, lanterns, n):
    l = m
  else:
    h = m

print(l)
