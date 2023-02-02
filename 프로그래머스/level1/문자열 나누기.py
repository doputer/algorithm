def solution(s):
  answer = 0
  start = 0

  while start < len(s) - 1:
    for i in range(start + 2, len(s) + 2, 2):
      if s[start: i].count(s[start]) * 2 == i - start:
        start = i
        answer += 1
        break
    else:
      start = i
      answer += 1

  return answer + 1 if start < len(s) else answer
