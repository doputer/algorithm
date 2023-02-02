def solution(s):
  answer = []
  prev = {}

  for i in range(len(s)):
    if s[i] not in prev:
      prev[s[i]] = i
      answer.append(-1)
    else:
      answer.append(i - prev[s[i]])
      prev[s[i]] = i

  return answer
