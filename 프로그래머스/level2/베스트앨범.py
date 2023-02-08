def solution(genres, plays):
  choice = [i for i in range(len(genres))]
  table = {}
  count = {}

  for i in range(len(genres)):
    if genres[i] in table:
      table[genres[i]] += plays[i]
      count[genres[i]] += 1
    else:
      table[genres[i]] = plays[i]
      count[genres[i]] = 1

  choice.sort(key=lambda x: (-table[genres[x]], -plays[x]))

  for genre in count.keys():
    if count[genre] >= 2:
      count[genre] = 2

  best = []

  for i in choice:
    if count[genres[i]] > 0:
      best.append(i)
      count[genres[i]] -= 1

  return best
