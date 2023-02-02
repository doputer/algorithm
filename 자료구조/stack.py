class Stack:
  def __init__(self, max):
    self.stack = [0 for i in range(max)]
    self.top = 0
    self.max = max

  def push(self, n):
    if self.isFull():
      return False

    self.stack[self.top] = n
    self.top += 1

  def pop(self):
    self.top -= 1
    item = self.stack[self.top]
    self.stack[self.top] = 0
    return item

  def peek(self):
    print(self.stack[self.top - 1])

  def isFull(self):
    if self.top == self.max:
      return True
    return False

  def print(self):
    print(self.stack)


stack = Stack(5)
