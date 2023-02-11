def sort(array):
  for i in range(1, len(array)):
    element = array[i]
    j = i - 1

    while j >= 0 and array[j] > element:
      array[j + 1] = array[j]
      j -= 1

    array[j + 1] = element

  return array
