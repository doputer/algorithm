n = int(input())
stock = list(map(int, input().split()))

maximum, profit = 0, 0

for i in range(len(stock) - 1, -1, -1):
    maximum = max(stock[i], maximum)
    profit = max(maximum - stock[i], profit)

print(profit)
