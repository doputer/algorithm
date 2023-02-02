def solution(chicken):
  coupon = 0

  while chicken >= 10:
    a, b = divmod(chicken, 10)

    coupon += a
    chicken = a + b

  return coupon
