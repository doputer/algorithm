def solution(babbling):
  count = 0

  for i in babbling:
    start = 0

    while True:
      if i.startswith("aya", start) or i.startswith("woo", start):
        start += 3
      elif i.startswith("ye", start) or i.startswith("ma", start):
        start += 2
      else:
        break

    if start == len(i):
      count += 1

  return count
