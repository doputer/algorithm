def solution(wallpaper):
    lux, luy = 50, 50
    rdx, rdy = -1, -1

    for x, row in enumerate(wallpaper):
        for y, file in enumerate(row):
            if file == '.':
                continue

            if x < lux:
                lux = x
            if y < luy:
                luy = y

            if x + 1 > rdx:
                rdx = x + 1
            if y + 1 > rdy:
                rdy = y + 1

    return [lux, luy, rdx, rdy]
