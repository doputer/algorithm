n = int(input())

dp = [1, 2]

for i in range(3, n + 1):
  if i ** 0.5 % 1 == 0:
    dp.append(1)
  else:
    dp.append(1 + min(dp[i - 1 - j ** 2] for j in range(1, int(i ** 0.5) + 1)))

print(dp[n - 1])
