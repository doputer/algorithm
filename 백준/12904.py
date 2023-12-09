s = input()
t = input()

flag = False

while len(s) <= len(t):
    if s == t:
        flag = True
        break

    if t[-1] == "A":
        t = t[:-1]
    else:
        t = t[:-1]
        t = t[::-1]

print(1 if flag else 0)
