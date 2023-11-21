def solution(park, routes):
    cx, cy = 0, 0
    width = len(park[0])
    height = len(park)

    for i in range(height):
        for j in range(width):
            if park[i][j] == "S":
                cx = j
                cy = i

    for route in routes:
        op, n = route.split(" ")
        n = int(n)

        if op == "E":
            if cx + n >= width:
                continue

            for nx in range(cx + 1, cx + n + 1):
                if park[cy][nx] == "X":
                    break
            else:
                cx += n
        elif op == "W":
            if cx - n < 0:
                continue

            for nx in range(cx - 1, cx - n - 1, -1):
                if park[cy][nx] == "X":
                    break
            else:
                cx -= n
        elif op == "N":
            if cy - n < 0:
                continue

            for ny in range(cy - 1, cy - n - 1, -1):
                if park[ny][cx] == "X":
                    break
            else:
                cy -= n
        else:
            if cy + n >= height:
                continue

            for ny in range(cy + 1, cy + n + 1):
                if park[ny][cx] == "X":
                    break
            else:
                cy += n

    return [cy, cx]
