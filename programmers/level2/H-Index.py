def solution(citations):
  citations.sort(reverse=True)

  length = len(citations)

  for i in range(length):
    citation = citations[i]

    if citation <= i:
      return i
  else:
    return length
