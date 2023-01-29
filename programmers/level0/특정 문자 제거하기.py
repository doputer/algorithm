def solution(my_string, letter):
  return ''.join(filter(lambda x: x != letter, my_string))
