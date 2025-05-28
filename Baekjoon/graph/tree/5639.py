import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def set_right(self, right):
        self.right = right

    def set_left(self, left):
        self.left = left

    def set_parent(self, parent):
        self.parent = parent

    def postorder(self):
        if self.left is not None: self.left.postorder()
        if self.right is not None: self.right.postorder()
        print(self.value)

    def preorder(self):
        print(self.value)
        if self.left is not None: self.left.preorder()
        if self.right is not None: self.right.preorder()

    def inorder(self):
        if self.left is not None: self.left.inorder()
        print(self.value)
        if self.right is not None: self.right.inorder()

values = []

while True:
    value = sys.stdin.readline().strip()
    if not value: break

    values.append(int(value))


root = Node(values[0])
root.set_parent(Node(float('inf')))
cur = root
for value in values[1:]:
    node = Node(value)

    if value < cur.value:
        cur.set_left(node)
        node.parent = cur
        cur = node
        continue

    while True:
        if cur.parent.value > value:
            cur = cur.parent
            continue
        cur.set_right(node)
        node.parent = cur
        break

    cur = node

# print(root)
# root.preorder()
# root.postorder()
root.inorder()
