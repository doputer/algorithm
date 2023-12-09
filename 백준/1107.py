from itertools import product

n = int(input())
m = int(input())

buttons = [str(i) for i in range(10)]

if m:
    errors = list(map(int, input().split(" ")))

    for error in errors:
        buttons.remove(str(error))

click = abs(100 - n)

for i in range(1, len(str(n)) + 2):
    for j in product(buttons, repeat=i):
        channel = "".join(j)
        click = min(click, len(str(int(channel))) + abs(n - int(channel)))

print(click)
