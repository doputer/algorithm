def merge(array, left, mid, right):
  temp = []
  i, j = left, mid

  while i < mid and j < right:
    if array[i] < array[j]:
      temp.append(array[i])
      i += 1
    else:
      temp.append(array[j])
      j += 1

  if i < mid:
    while i < mid:
      temp.append(array[i])
      i += 1

  if j < right:
    while j < right:
      temp.append(array[j])
      j += 1

  for i in range(left, right):
    array[i] = temp[i - left]


def divide(array, left, right):
  if right - left < 2:
    return

  mid = (right + left) // 2

  divide(array, left, mid)
  divide(array, mid, right)
  merge(array, left, mid, right)


def sort(array):
  return divide(array, 0, len(array))

# def merge(left, right):
#   temp = []
#   i, j = 0, 0

#   while i < len(left) and j < len(right):
#     if left[i] < right[j]:
#       temp.append(left[i])
#       i += 1
#     else:
#       temp.append(right[j])
#       j += 1

#   temp += left[i:]
#   temp += right[j:]

#   return temp


# def sort(array):
#   mid = len(array) // 2

#   if mid == 0:
#     return array

#   left = sort(array[:mid])
#   right = sort(array[mid:])

#   return merge(left, right)
