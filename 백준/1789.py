s = int(input())

total = 0
count = 0

for i in range(1, s + 1):
    if s - total < i:
        break
    else:
        total += i
        count += 1

print(count)
