def solution(spell, dic):
  s = set(spell)
  l = len(s)

  for i in dic:
    if len(set(i) - s) == 0 and len(set(i)) == l:
      return 1

  return 2
