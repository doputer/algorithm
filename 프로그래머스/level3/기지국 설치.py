def plant(l, w):
  l, mod = divmod(l, w * 2 + 1)

  return l + 1 if mod else l


def solution(n, stations, w):
  count = 0

  if stations[0] != 1:
    count += plant(stations[0] - w - 1, w)

  for i in range(len(stations) - 1):
    count += plant((stations[i + 1] - w - 1) - (stations[i] + w + 1) + 1, w)

  if stations[-1] != n:
    count += plant(n - stations[-1] - w, w)

  return count
