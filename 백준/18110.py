import sys


def new_round(val):
    return int(val) + 1 if val - int(val) >= 0.5 else int(val)


input = sys.stdin.readline
n = int(input())

if n:
    scores = [int(input()) for _ in range(n)]

    cut = new_round(n * 0.15)
    scores.sort()

    print(new_round(sum(scores[cut:-cut] if cut else scores) / (n - cut * 2)))
else:
    print(0)
