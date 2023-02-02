class Queue:
  def __init__(self, max):
    self.head = 0
    self.rear = 0
    self.max = max
    self.queue = [0 for i in range(max)]

  def enqueue(self, n):
    if self.isFull():
      return False

    self.queue[self.rear] = n
    self.rear += 1

  def dequeue(self):
    if self.head + 1 > self.rear:
      return False

    item = self.queue[self.head]
    self.queue[self.head] = 0
    self.head += 1
    return item

  def isFull(self):
    if self.rear == self.max:
      return True
    return False

  def print(self):
    print(self.queue)


queue = Queue(5)
