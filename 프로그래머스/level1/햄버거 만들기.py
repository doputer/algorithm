def solution(ingredient):
  answer = 0
  temp = []

  for i in ingredient:
    temp.append(i)

    if i == 1 and [1, 2, 3, 1] == temp[-4:]:
      answer += 1
      [temp.pop() for _ in range(4)]

  return answer
