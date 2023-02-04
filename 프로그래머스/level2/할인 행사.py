def solution(want, number, discount):
  count = 0
  discounts = {}

  for i in range(len(discount)):
    if discount[i] in discounts:
      discounts[discount[i]] += 1
    else:
      discounts[discount[i]] = 1

    if i >= 10:
      discounts[discount[i - 10]] -= 1

    if i >= 9:
      for j in range(len(want)):
        if want[j] not in discounts or discounts[want[j]] < number[j]:
          break
      else:
        count += 1

  return count
