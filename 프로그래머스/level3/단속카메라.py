def solution(routes):
  count = 1

  routes.sort(key=lambda x: x[1])
  prev_out = routes[0][1]

  for i in range(1, len(routes)):
    curr_in, curr_out = routes[i]

    if curr_in > prev_out:
      prev_out = curr_out
      count += 1

  return count
