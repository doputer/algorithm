def sort(array):
  for i in range(len(array)):
    element = min(array[i:])
    index = array[i:].index(element)

    if index:
      array[i], array[index + i] = array[index + i], array[i]

  return array
