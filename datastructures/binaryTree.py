from datastructures.queue import Queue


class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insertLeft(self, newNode):
        if not self.left:
            self.left = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.left = self.left
            self.left = tree

    def insertRight(self, newNode):
        if not self.right:
            self.right = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.right = self.right
            self.right = tree

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
