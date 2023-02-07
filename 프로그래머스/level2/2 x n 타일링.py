def solution(n):
  dp = [1, 1]

  for i in range(2, n + 1):
    dp.append((dp[i - 1] + dp[i - 2]) % 1000000007)

  return dp[-1]

# def solution(n):
#     a, b = 1, 1

#     for _ in range(n - 1):
#         a, b = b, (a + b) % 1000000007

#     return b
