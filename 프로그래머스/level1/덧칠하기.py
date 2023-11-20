def solution(n, m, section):
    count = 1
    paint = section[0]

    for area in section:
        if area >= paint + m:
            paint = area
            count += 1

    return count
