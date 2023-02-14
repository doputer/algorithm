n, m, b = map(int, input().split())

ground = []

for _ in range(n):
  blocks = list(map(int, input().split()))

  for block in blocks:
    ground.append(block)


time = int(1e9)
height = 0

flat = max(ground)

while flat >= 0:
  up = 0
  down = 0

  for i in ground:
    if i > flat:
      up += i - flat
    elif i < flat:
      down += flat - i

  if b + up >= down and up * 2 + down < time:
    time = up * 2 + down
    height = flat

  flat -= 1

print(time, height)
