def rotate(s, n):
  return s[-n:] + s[:-n]


def solution(A, B):
  count = 0

  for i in range(len(A)):
    if rotate(A, i) == B:
      return count

    count += 1

  return -1
