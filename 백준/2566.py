l = [list(map(int, input().split())) for _ in range(9)]

maximum = -1
x, y = -1, -1

for i, row in enumerate(l):
    for j, col in enumerate(row):
        if maximum < col:
            maximum = col
            x, y = i + 1, j + 1

print(maximum)
print(x, y)
