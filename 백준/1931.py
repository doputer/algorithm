def solution():
    n = int(input())

    rooms = []

    for _ in range(n):
        rooms.append(list(map(int, input().split())))

    rooms.sort(key=lambda x: (x[1], x[0]))

    time = 0
    count = 0

    for start, end in rooms:
        if time == 0:
            time = end
            count += 1
        elif time <= start:
            time = end
            count += 1

    return count


print(solution())
