import sys

n = int(sys.stdin.readline())
coords = list(map(int, sys.stdin.readline().split()))

ranks = {}
rank = 0

sorted_coords = sorted(coords)

for i in range(n):
    if i != 0 and sorted_coords[i] > sorted_coords[i - 1]:
        rank += 1

    if sorted_coords[i] not in ranks:
        ranks[sorted_coords[i]] = rank

print(*[ranks[i] for i in coords])
