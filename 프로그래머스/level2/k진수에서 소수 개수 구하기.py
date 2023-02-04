def base(n, k):
  res = ''

  while n > 0:
    n, mod = divmod(n, k)
    res += str(mod)

  return res[::-1]


def isPrime(n):
  if n == 1:
    return False

  m = int(n ** 0.5) + 1

  for i in range(2, m):
    if n % i == 0:
      return False

  return True


def solution(n, k):
  count = 0
  n = base(n, k)
  mode = True
  temp = ''

  for i in n:
    if i == '0':
      mode = False

      if temp != '' and isPrime(int(temp)):
        count += 1

      temp = ''
    else:
      mode = True

    if mode:
      temp += i
  else:
    if temp != '' and isPrime(int(temp)):
      count += 1

  return count
