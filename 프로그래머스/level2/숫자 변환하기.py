def solution(x, y, n):
  dp = [0] * (y+1)

  dp[x] = 1

  for i in range(x, y+1):
    if dp[i]:
      if i*2 <= y:
        dp[i*2] = min(dp[i*2], dp[i]+1) if dp[i*2] else dp[i]+1
      if i*3 <= y:
        dp[i*3] = min(dp[i*3], dp[i]+1) if dp[i*3] else dp[i]+1
      if i+n <= y:
        dp[i+n] = min(dp[i+n], dp[i]+1) if dp[i+n] else dp[i]+1

  return dp[y]-1 if dp[y] else -1
