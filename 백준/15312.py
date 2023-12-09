a = input()
b = input()

stroke = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
alphabet = {chr(i + 65): stroke[i] for i in range(26)}

n = len(a) * 2
numbers = []

for i in range(n // 2):
    numbers.append(alphabet[a[i]])
    numbers.append(alphabet[b[i]])

while n > 2:
    for i in range(n - 1):
        numbers[i] = (numbers[i] + numbers[i + 1]) % 10

    n -= 1

print("".join(list(map(str, numbers[:2]))))
