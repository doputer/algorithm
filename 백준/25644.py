def dp(stock):
  if len(stock) <= 1:
    return 0

  minimum = min(stock)
  index = stock.index(minimum)

  if index == 0:
    return stock[-1] - stock[0]

  left = dp(stock[:index])
  right = dp(stock[index:])

  return left if left > right else right


n = int(input())
stock = list(map(int, input().split()))

print(dp(stock))
