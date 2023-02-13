def check(m, c, wifi):
  prev = wifi[0]
  count = 1

  for i in range(1, len(wifi)):
    if wifi[i] - prev >= m:
      prev = wifi[i]
      count += 1

      if count >= c:
        return True

  return False


n, c = map(int, input().split())

wifi = []

for _ in range(n):
  wifi.append(int(input()))

wifi.sort()

l, h = 1, wifi[-1] - wifi[0] + 1

while l + 1 < h:
  m = (l + h) // 2

  if check(m, c, wifi):
    l = m
  else:
    h = m

print(l)
