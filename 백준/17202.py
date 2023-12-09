a = input()
b = input()

n = 16
numbers = []

for i in range(8):
    numbers.append(int(a[i]))
    numbers.append(int(b[i]))

while n > 2:
    for i in range(1, n):
        numbers[i - 1] = (numbers[i - 1] + numbers[i]) % 10

    n -= 1

print("".join(list(map(str, numbers[:2]))))
