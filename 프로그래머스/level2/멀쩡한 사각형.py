from math import ceil, floor


def solution(w, h):
  if w < h:
    w, h = h, w

  cut = 0
  x = 0
  def y(y): return y * w / h

  for i in range(h):
    nx = y(i + 1)
    cut += ceil(nx) - x
    x = floor(nx)

    if nx % 1 == 0:
      break

  return w * h - (cut * h // (i + 1))
