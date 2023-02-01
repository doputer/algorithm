def borrow(index, lost, reserve):
  if index >= len(lost):
    return len(lost) - lost.count(0)

  if lost[index] - 1 in reserve and lost[index] not in reserve:
    reserve[reserve.index(lost[index] - 1)] = 0
    lost[index] = 0

  if lost[index] + 1 in reserve and lost[index] not in reserve:
    reserve[reserve.index(lost[index] + 1)] = 0
    lost[index] = 0

  return borrow(index + 1, lost, reserve)


def solution(n, lost, reserve):
  return n - borrow(0, list(set(lost) - set(reserve)), list(set(reserve) - set(lost)))
