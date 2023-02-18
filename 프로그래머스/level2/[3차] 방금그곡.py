def getMinute(time):
  hour, minute = time.split(':')

  return int(hour) * 60 + int(minute)


def getPlaytime(start_time, end_time):
  return getMinute(end_time) - getMinute(start_time)


def getMelody(m):
  return m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')


def solution(m, musicinfos):
  m = getMelody(m)

  answer = ('', 0)

  for info in musicinfos:
    start_time, end_time, title, melody = info.split(',')

    playtime = getPlaytime(start_time, end_time)
    melody = getMelody(melody)
    melody = ''.join(melody[i % len(melody)] for i in range(playtime))

    if m in melody and playtime > answer[1]:
      answer = (title, playtime)

  return "(None)" if answer == ('', 0) else answer[0]
