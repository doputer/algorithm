def solution(i, j, k):
  count = 0

  for i in range(i, j + 1):
    count += str(i).count(str(k))

  return count
