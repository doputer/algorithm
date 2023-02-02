def solution(n):
  memo = [1, 1]
  memo.extend([0 for _ in range(2000)])

  for i in range(2, n + 1):
    memo[i] = memo[i - 1] + memo[i - 2]

  return memo[n] % 1234567
