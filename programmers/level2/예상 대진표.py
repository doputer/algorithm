def solution(n, a, b):
  answer = 1

  while True:
    if abs(a - b) == 1 and min(a, b) % 2 != 0 and max(a, b) % 2 != 1:
      return answer

    a = (a + 1) // 2
    b = (b + 1) // 2
    answer += 1
