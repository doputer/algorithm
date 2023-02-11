from random import shuffle
from time import time

import insertion
import selection
import bubble
import merge


def measure(array, sort):
  start_time = time()
  sort(array)
  end_time = time()

  print(end_time - start_time)


array = [i for i in range(5000)]
shuffle(array)

measure(array[:], insertion.sort)
measure(array[:], selection.sort)
measure(array[:], bubble.sort)
measure(array[:], merge.sort)
