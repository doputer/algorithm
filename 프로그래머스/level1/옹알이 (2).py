def solution(babbling):
  words = ["aya", "ye", "woo", "ma"]
  count = 0

  for word in babbling:
    last = ''

    while word[:2] in words or word[:3] in words:
      if word[:2] in words:
        if last == word[:2]:
          break

        last = word[:2]
        word = word[2:]
      else:
        if last == word[:3]:
          break

        last = word[:3]
        word = word[3:]

    if len(word) == 0:
      count += 1

  return count
