n = int(input())
seq = list(map(int, input().split()))

length = 0
left, right = 0, 0
prev = seq[1] * (seq[1] - seq[0])

for i in range(1, len(seq)):
    curr = seq[i] * (seq[i] - seq[i - 1])

    print(prev, curr)

    if prev >= 0 and curr >= 0 or prev <= 0 and curr <= 0:
        right += 1
        print(1)
    else:
        length = max(right - left + 1, length)
        right += 1
        left = right
        print(2)

    prev = curr

print(length)
