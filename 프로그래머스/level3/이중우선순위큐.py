class Max_Heap:
  def __init__(self, array):
    self.heap = [0] + array
    self.size = len(array)

    for i in range(self.size // 2, 0, -1):
      self.heapify(i)

  def heapify(self, i):
    largest = i
    left = i * 2
    right = i * 2 + 1

    if left <= self.size and self.heap[largest] < self.heap[left]:
      largest = left
    if right <= self.size and self.heap[largest] < self.heap[right]:
      largest = right

    if i != largest:
      self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
      self.heapify(largest)

  def insert(self, n):
    self.size += 1
    self.heap.append(n)

    i = self.size

    while i > 1 and self.heap[i] > self.heap[i // 2]:
      self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
      i //= 2

  def extract(self):
    if self.size == 0:
      return

    largest = self.peek()

    self.size -= 1

    if self.size == 0:
      return self.heap.pop()

    self.heap[1] = self.heap.pop()
    self.heapify(1)

    return largest

  def increase(self, n):
    if self.size == 0:
      return

    i = self.heap.index(n)

    self.heap[i] = float('inf')

    while i > 1 and self.heap[i] > self.heap[i // 2]:
      self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
      i //= 2

    self.extract()

  def peek(self):
    return self.heap[1]

  def show(self):
    return self.heap[1:]


class Min_Heap:
  def __init__(self, array):
    self.heap = [0] + array
    self.size = len(array)

    for i in range(self.size // 2, 0, -1):
      self.heapify(i)

  def heapify(self, i):
    smallest = i
    left = i * 2
    right = i * 2 + 1

    if left <= self.size and self.heap[smallest] > self.heap[left]:
      smallest = left
    if right <= self.size and self.heap[smallest] > self.heap[right]:
      smallest = right

    if i != smallest:
      self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
      self.heapify(smallest)

  def insert(self, n):
    self.size += 1
    self.heap.append(n)

    i = self.size

    while i > 1 and self.heap[i] < self.heap[i // 2]:
      self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
      i //= 2

  def extract(self):
    if self.size == 0:
      return

    smallest = self.peek()

    self.size -= 1

    if self.size == 0:
      return self.heap.pop()

    self.heap[1] = self.heap.pop()
    self.heapify(1)

    return smallest

  def decrease(self, n):
    if self.size == 0:
      return

    i = self.heap.index(n)

    self.heap[i] = float('-inf')

    while i > 1 and self.heap[i] < self.heap[i // 2]:
      self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
      i //= 2

    self.extract()

  def peek(self):
    return self.heap[1]

  def show(self):
    return self.heap[1:]


class Priority_Queue:
  def __init__(self):
    self.max_heap = Max_Heap([])
    self.min_heap = Min_Heap([])

  def enqueue(self, n):
    self.max_heap.insert(n)
    self.min_heap.insert(n)

  def max_dequeue(self):
    maximum = self.max_heap.extract()
    self.min_heap.decrease(maximum)

  def min_dequeue(self):
    minimum = self.min_heap.extract()
    self.max_heap.increase(minimum)

  def show(self):
    max_heap = self.max_heap.show()
    min_heap = self.min_heap.show()

    if len(max_heap) == 0:
      return [0, 0]
    else:
      return [max_heap[0], min_heap[0]]


def solution(operations):
  queue = Priority_Queue()

  for operation in operations:
    n, m = operation.split(' ')

    if n == 'I':
      queue.enqueue(int(m))
    else:
      if m == '1':
        queue.max_dequeue()
      else:
        queue.min_dequeue()

  return queue.show()
