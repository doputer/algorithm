def solution(num, total):
  if num % 2 == 0:
    n = (total - num * (num - 1) // 2) // num
  else:
    n = total // num - num // 2

  return [i for i in range(n, n + num)]
