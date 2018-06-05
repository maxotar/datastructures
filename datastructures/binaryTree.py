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

        # # Alternative method using extend
        # nodes = []
        # nodes.append(self.data)
        # nodes.extend(self.left.preorder()) if self.left else()
        # nodes.extend(self.right.preorder()) if self.right else()
        # return nodes

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
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            nodes = next_nodes

        return output

# nests = [1, 2, [3, 4, [5],['hi']], [6, [[[7, 'hello']]]]]

# def flatten(container):
#     for i in container:
#         if isinstance(i, (list,tuple)):
#             for j in flatten(i):
#                 yield j
#         else:
#             yield i

# print list(flatten(nests))


# flatten list and performance https://stackoverflow.com/a/45323085
# Iterator --> https://stackoverflow.com/questions/19151/build-a-basic-python-iterator#24377
# Amazing --> https://codereview.stackexchange.com/questions/183942/use-generator-to-do-inorder-traversal
# Very good --> http://thatmattbone.com/binary-tree-traversal-in-python-with-generators.html
# https://github.com/joowani/binarytree
# https://medium.com/the-renaissance-developer/learning-tree-data-structure-27c6bb363051
# https://www.geeksforgeeks.org/?p=2686
