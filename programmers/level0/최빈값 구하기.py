def solution(array):
  modes = {}

  for i in set(array):
    modes[i] = array.count(i)

  max_mode = max(modes.values())

  if list(modes.values()).count(max_mode) > 1:
    return -1

  for i in modes.keys():
    if modes[i] == max_mode:
      return i
