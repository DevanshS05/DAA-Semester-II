class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def getNewNode(self, value):
        return node(value)

    def addLeftChild(self, value):
        if self.left is None:
            self.left = self.getNewNode(value)
        else:
            print("Left child already exists!")

    def addRightChild(self, value):
        if self.right is None:
            self.right = self.getNewNode(value)
        else:
            print("Right child is already present")

class Tree:
    def __init__(self):
        self.root = None

root = node(5)
root.addLeftChild(4)
root.addRightChild(6)
root.left.addLeftChild(2)
root.left.addRightChild(4.5)

print(root.left.right.value)
