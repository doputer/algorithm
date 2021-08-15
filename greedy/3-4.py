n, k = map(int, input().split())
count = 0

while True:
    while n % k == 0:
        n /= k
        count += 1

    if n == 1:
        break

    count += n % k
    n -= n % k

print(count)
