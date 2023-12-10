def rate(play, win):
    return (win * 100) // play


x, y = map(int, input().split(" "))
z = rate(x, y)

low = 0
high = 1e9
ans = -1

while low <= high:
    mid = (low + high) // 2

    if z < rate(x + mid, y + mid):
        high = mid - 1
        ans = mid
    else:
        low = mid + 1

print(int(ans))
