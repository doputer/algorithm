class Heap:
  def __init__(self, array):
    self.heap = [0] + array
    self.size = len(array)

    for i in range(self.size // 2, 0, -1):
      self.heapify(i)

    print(self.heap[1:])

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

    print("{0:<2} -> {1}".format(n, self.heap[1:]))

  def extract(self):
    largest = self.peek()

    self.size -= 1
    self.heap[1] = self.heap.pop()
    self.heapify(1)

    print("{0:<2} <- {1}".format(largest, self.heap[1:]))

  def peek(self):
    return self.heap[1]


heap = Heap([5, 7, 13, 15, 20])

heap.insert(17)
heap.extract()
