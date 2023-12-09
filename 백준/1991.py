class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class Tree:
    def __init__(self, head):
        self.head = head


n = int(input())

for _ in range(n):
    node, left, right = input().split()
