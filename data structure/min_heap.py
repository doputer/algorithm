class Heap:
  def __init__(self):
    self.heap = [0]
    self.n = 1

  def getLeftChild(self, i):
    if i * 2 >= self.n:
      return -1

    return i * 2

  def getRightChild(self, i):
    if i * 2 + 1 >= self.n:
      return -1

    return i * 2 + 1

  def upHeap(self, i):
    while i > 0:
      if self.heap[i] < self.heap[int(i / 2)]:
        self.heap[i], self.heap[int(i / 2)] = self.heap[int(i / 2)], self.heap[i]
      i = int(i / 2)

  def downHeap(self, i):
    if self.getLeftChild(i) == -1 and self.getRightChild(i) == -1:
      return

    smaller = self.getLeftChild(i)

    if self.getRightChild(i) != -1:
      if self.heap[smaller] > self.heap[self.getRightChild(i)]:
        smaller = self.getRightChild(i)

    if self.heap[i] < self.heap[smaller]:
      return

    self.heap[i], self.heap[smaller] = self.heap[smaller], self.heap[i]

    self.downHeap(smaller)

  def insertItem(self, key):
    self.heap.append(key)
    self.upHeap(self.n)
    self.n += 1

  def removeMin(self):
    self.heap[1] = self.heap.pop()
    self.n -= 1
    self.downHeap(1)

  def printHeap(self):
    print(self.heap[1:])


H = Heap()

while True:
  inp = input().split()

  if inp[0] == 'i':
    H.insertItem(int(inp[1]))
  elif inp[0] == 'd':
    H.removeMin()
  elif inp[0] == 'p':
    H.printHeap()
  elif inp[0] == 'q':
    break
