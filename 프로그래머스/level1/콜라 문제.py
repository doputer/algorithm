def solution(a, b, n):
  answer = 0

  while n >= a:
    fill, empty = divmod(n, a)

    n = fill * b + empty

    answer += fill * b

  return answer
