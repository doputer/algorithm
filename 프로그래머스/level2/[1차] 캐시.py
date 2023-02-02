def solution(cacheSize, cities):
  if cacheSize == 0:
    return len(cities) * 5

  answer = 0
  l = []

  for city in cities:
    city = city.lower()

    if city in l:
      answer += 1

      l.remove(city)
      l.insert(0, city)
    else:
      answer += 5

      if len(l) == cacheSize:
        l.pop()
      l.insert(0, city)

  return answer
