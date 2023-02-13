def cut(mid, m, trees):
  return sum(tree - mid for tree in trees if tree > mid) >= m


n, m = map(int, input().split())
trees = list(map(int, input().split()))

low, high = 0, int(1e9)

while low + 1 < high:
  mid = (low + high) // 2

  print(low, mid, high)

  if cut(mid, m, trees):
    low = mid
  else:
    high = mid

print(low)
