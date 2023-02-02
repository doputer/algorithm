from re import sub


def solution(my_string):
  return sub('[aeiou]', '', my_string)
