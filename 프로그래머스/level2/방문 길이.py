def solution(dirs):
  routes = []
  curr = (0, 0)

  for dir in dirs:
    x, y = curr
    nx, ny = curr

    if dir == 'U':
      ny += 1
    elif dir == 'D':
      ny -= 1
    elif dir == 'R':
      nx += 1
    else:
      nx -= 1

    route = ((x, y), (nx, ny))

    if -5 <= nx <= 5 and -5 <= ny <= 5:
      if route not in routes and route[::-1] not in routes:
        routes.append(route)
        routes.append(route[::-1])

      curr = (nx, ny)

  return len(routes) // 2
