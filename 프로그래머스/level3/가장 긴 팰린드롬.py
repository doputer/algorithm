def solution(s):
  answer = 0

  for i in range(len(s)):
    for j in range(i, len(s)):
      if s[i:j+1] == s[i:j+1][::-1]:
        answer = max(j-i+1, answer)

  return answer
