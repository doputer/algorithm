from collections import deque

t = int(input())

for _ in range(t):
    p = list(input())
    n = int(input())
    s = input()

    if n:
        l = deque(s[1:-1].split(","))
    else:
        l = deque()

    flag = True
    flip = False

    for i in p:
        if i == "R":
            flip = not flip
        else:
            if not len(l):
                flag = False
                break

            if flip:
                l.pop()
            else:
                l.popleft()

    if flag:
        if flip:
            l.reverse()

        print(f"[{','.join(map(str, l))}]")
    else:
        print("error")
