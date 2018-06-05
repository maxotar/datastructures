class BinarySearchTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
        if data <= self.data and self.left:
            self.left.insert(data)
        elif data <= self.data:
            self.left = BinarySearchTree(data)
        elif data > self.data and self.right:
            self.right.insert(data)
        else:
            self.right = BinarySearchTree(data)

    def search(self, item):
        if item < self.data and self.left:
            return self.left.search(item)
        if item > self.data and self.right:
            return self.right.search(item)
        return item == self.data

    def min(self):
        return self.left.min() if self.left else self.data

    def max(self):
        return self.right.max() if self.right else self.data
