from itertools import combinations


def solution(orders, course):
  menus = []

  for n in course:
    courses = {}
    maximum = 0

    for order in orders:
      for menu in combinations(order, n):
        menu = ''.join(sorted(menu))

        if menu in courses:
          courses[menu] += 1
        else:
          courses[menu] = 1

        maximum = max(courses[menu], maximum)

    for key, value in courses.items():
      if value == maximum and value > 1:
        menus.append(key)

  return sorted(menus)
