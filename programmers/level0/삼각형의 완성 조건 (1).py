def solution(sides):
  side = sides.pop(sides.index(max(sides)))

  return 1 if sum(sides) > side else 2
