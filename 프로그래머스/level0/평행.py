def solution(dots):
  angles = set()

  for i in range(3):
    for j in range(i + 1, 4):
      x1, y1 = dots[i]
      x2, y2 = dots[j]

      angle = (x1 - x2) / (y1 - y2)

      if angle in angles:
        return 1

      angles.add(angle)

  return 0
