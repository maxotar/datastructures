from datastructures.queue import Queue


class BinarySearchTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
        if data < self.data and self.left:
            self.left.insert(data)
        elif data < self.data:
            self.left = BinarySearchTree(data)
        elif data > self.data and self.right:
            self.right.insert(data)
        elif data > self.data:
            self.right = BinarySearchTree(data)
        return self

    def search(self, item):
        if item < self.data and self.left:
            return self.left.search(item)
        elif item > self.data and self.right:
            return self.right.search(item)
        return item == self.data

    def preorder(self):
        yield self.data
        yield from self.left.preorder() if self.left else()
        yield from self.right.preorder() if self.right else()

    def inorder(self):
        yield from self.left.inorder() if self.left else()
        yield self.data
        yield from self.right.inorder() if self.right else()

    def postorder(self):
        yield from self.left.postorder() if self.left else()
        yield from self.right.postorder() if self.right else()
        yield self.data

    def levelorder(self):
        myq = Queue()
        myq.enqueue(self)
        while not myq.isEmpty():
            cur = myq.dequeue()
            yield cur.data
            myq.enqueue(cur.left) if cur.left else()
            myq.enqueue(cur.right) if cur.right else()

    def levelordernested(self):
        output = []
        nodes = [self]
        while nodes:
            output.append([node.data for node in nodes])
            next_nodes = []
            for node in nodes:
                next_nodes.append(node.left) if node.left else()
                next_nodes.append(node.right) if node.right else()
            nodes = next_nodes

        return output

    def minValue(self):
        return self.left.minValue() if self.left else self.data

    def maxValue(self):
        return self.right.maxValue() if self.right else self.data

    def minNode(self):
        return self.left.minNode() if self.left else self

    def maxNode(self):
        return self.right.maxNode() if self.right else self

    def remove(self, item):
        if item < self.data:
            self.left = self.left.remove(item)
        elif item > self.data:
            self.right = self.right.remove(item)
        else:  # item == data
            if not self.left:
                return self.right
            elif not self.right:
                return self.left
            else:  # Node with two children
                # Get the inorder successor (smallest in the right subtree)
                temp = self.right.minNode()
                # Copy the inorder successor's content to this node
                self.data = temp.data
                # Delete the inorder successor
                self.right = self.right.remove(temp.data)
        return self

    def height(self):
        if self.left:
            heightLeft = self.left.height()
        else:
            heightLeft = 0
        if self.right:
            heightRight = self.right.height()
        else:
            heightRight = 0
        return 1 + max(heightLeft, heightRight)

    def toList(self):
        return list(self.levelorder())

    def __str__(self):
        return str(list(self.levelorder()))
