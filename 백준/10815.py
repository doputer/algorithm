n = int(input())

cards = set(map(int, input().split()))

m = int(input())

check = list(map(lambda x: 1 if x in cards else 0, list(map(int, input().split()))))

print(*check)
