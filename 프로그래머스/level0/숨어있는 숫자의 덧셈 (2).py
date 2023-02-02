def solution(my_string):
  answer = 0
  n = 0

  for i in range(len(my_string)):
    if my_string[i].isdigit():
      if n > 0:
        n *= 10
      n += int(my_string[i])
    else:
      answer += n
      n = 0

  answer += n

  return answer
