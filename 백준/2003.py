n, m = map(int, input().split(" "))

a = [0] + list(map(int, input().split(" ")))
s = [0] * (n + 1)

for i in range(1, n + 1):
    s[i] = s[i - 1] + a[i]

left, right = 0, 0
total = 0
count = 0

while left < n or right < n:
    sub_total = s[right] - s[left]

    if sub_total == m:
        count += 1

    if right == n:
        left += 1
    else:
        if sub_total < m:
            right += 1
        elif sub_total >= m:
            left += 1

print(count)
