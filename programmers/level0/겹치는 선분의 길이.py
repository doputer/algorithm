def solution(lines):
  for i in range(len(lines)):
    start, end = lines[i]
    lines[i] = set(list(range(start, end + 1)))

  a, b, c = lines
  a, b, c, d = len(a & b), len(b & c), len(a & c), len(a & b & c)

  if d:
    d = (d - 1) * 2

  return a + b + c - (3 - [a, b, c].count(0)) - d
