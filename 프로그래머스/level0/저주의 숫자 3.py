def passSam(n):
  return passSam(n + 1) if '3' in str(n) or n % 3 == 0 else n


def solution(n):
  sam = 0

  for _ in range(n):
    sam += 1
    sam = passSam(sam)

  return sam
