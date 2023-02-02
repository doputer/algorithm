def solution(price):
  discount = 1

  if price >= 500000:
    discount = 0.8
  elif price >= 300000:
    discount = 0.9
  elif price >= 100000:
    discount = 0.95

  return int(price * discount)
