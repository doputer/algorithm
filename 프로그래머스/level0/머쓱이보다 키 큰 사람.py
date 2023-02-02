def solution(array, height):
  return sum([i > height for i in array])
