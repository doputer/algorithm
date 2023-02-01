def solution(numer1, denom1, numer2, denom2):
  a = numer1 * denom2 + numer2 * denom1
  b = denom1 * denom2

  while True:
    for i in range(2, min(a, b) + 1):
      if a % i == 0 and b % i == 0:
        a //= i
        b //= i
        break
    else:
      break

  return [a, b]
