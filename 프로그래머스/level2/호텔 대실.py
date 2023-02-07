def getTime(s):
  hour, minute = map(int, s.split(':'))

  return hour * 60 + minute


def solution(book_time):
  rooms = []

  book_time.sort()

  for time in book_time:
    for i in range(len(rooms)):
      if getTime(rooms[i][-1][1]) + 10 <= getTime(time[0]):
        rooms[i].append(time)
        break
    else:
      rooms.append([time])

  return len(rooms)
