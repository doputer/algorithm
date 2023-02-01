def solution(s):
  s = s.replace('{', '')
  s = s.replace('}', '')
  s = list(map(lambda x: int(x), s.split(',')))
  l = list(set(s))
  l.sort(key=lambda x: s.count(x), reverse=True)

  return l
