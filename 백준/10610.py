n = list(input())

if sum(int(i) for i in n) % 3 == 0 and "0" in n:
    print("".join(sorted(n, reverse=True)))
else:
    print(-1)
