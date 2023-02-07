from collections import deque


def solution(bridge_length, weight, truck_weights):
  time = 0

  truck_weights = deque(truck_weights)
  bridge = deque()
  bridge_weight = 0

  while truck_weights or bridge:
    while truck_weights and len(bridge) < bridge_length and bridge_weight + truck_weights[0] <= weight:
      time += 1
      bridge_weight += truck_weights[0]
      bridge.append((time, truck_weights.popleft()))

      if bridge[0][0] + bridge_length == time:
        truck_in, truck_weight = bridge.popleft()
        bridge_weight -= truck_weight

    truck_in, truck_weight = bridge.popleft()
    time = truck_in + bridge_length - 1
    bridge_weight -= truck_weight

  return time + 1
