n, k = map(int, input().split())

temp = list(map(int, input().split()))

print(max(sum(temp[i : i + k]) for i in range(n - k + 1)))
