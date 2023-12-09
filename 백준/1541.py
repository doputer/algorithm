exp = input()

res = 0
n = 0
mode = 1

for i in exp:
    if i.isdigit():
        n = n * 10 + int(i)
    else:
        res += n if mode == 1 else -n
        n = 0

        if i == "-":
            mode = -1
else:
    res += n if mode == 1 else -n

print(res)
