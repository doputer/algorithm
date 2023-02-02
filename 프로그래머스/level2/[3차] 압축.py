def solution(msg):
  answer = []
  hash = {}
  last_index = 27
  start = 0
  end = start + 1

  for i in range(1, last_index):
    hash[chr(i + 64)] = i

  while start < len(msg) and end <= len(msg):
    while msg[start:end] in hash and end <= len(msg):
      end += 1

    answer.append(hash[msg[start:end-1]])
    hash[msg[start:end]] = last_index
    last_index += 1

    start = end - 1

  return answer
