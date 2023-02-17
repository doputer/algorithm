def solution(cards1, cards2, goal):
  i, j, k = 0, 0, 0

  while True:
    if i < len(cards1) and k < len(goal) and cards1[i] == goal[k]:
      i += 1
    elif j < len(cards2) and k < len(goal) and cards2[j] == goal[k]:
      j += 1
    else:
      break

    k += 1

  return 'Yes' if k == len(goal) else 'No'
