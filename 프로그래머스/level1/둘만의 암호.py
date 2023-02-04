def solution(s, skip, index):
  skip = [ord(i) for i in skip]
  s = list(s)

  for i in range(len(s)):
    count = 1

    while count <= index:
      a, b = divmod(ord(s[i]) + 1, 123)

      if 97 * a + b not in skip:
        count += 1
      s[i] = chr(97 * a + b)

  return ''.join(s)
