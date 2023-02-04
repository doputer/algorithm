def getCost(use, fees):
  if use <= fees[0]:
    cost = fees[1]
  else:
    a, b = divmod(use - fees[0], fees[2])

    if b > 0:
      a += 1

    cost = fees[1] + fees[3] * a

  return cost


def solution(fees, records):
  answer = []

  uses = {}

  for record in records:
    time, number, inout = record.split(" ")

    hour, minute = time.split(":")
    curr_time = int(hour) * 60 + int(minute)

    if inout == "IN":
      if number in uses:
        uses[number] -= curr_time
      else:
        uses[number] = -curr_time
    else:
      uses[number] += curr_time

  for k, v in uses.items():
    if v <= 0:
      uses[k] = getCost(v + 1439, fees)
    else:
      uses[k] = getCost(v, fees)

  return [uses[k] for k in sorted(uses.keys())]
