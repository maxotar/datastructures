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
        if self.left:
            for nodeData in self.left.preorder():
                yield nodeData
        if self.right:
            for nodeData in self.right.preorder():
                yield nodeData

        # #Alternative method using extend
        # nodes = []
        # if self:
        #     nodes.append(self.data)
        #     if self.left:
        #         nodes.extend(self.left.preorder())
        #     if self.right:
        #         nodes.extend(self.right.preorder())
        # return nodes

    def inorder(self):
        if self.left:
            for nodeData in self.left.inorder():
                yield nodeData
        yield self.data
        if self.right:
            for nodeData in self.right.inorder():
                yield nodeData

    def postorder(self):
        if self.left:
            for nodeData in self.left.postorder():
                yield nodeData
        if self.right:
            for nodeData in self.right.postorder():
                yield nodeData
        yield self.data


if __name__ == "__main__":
    a = BinaryTree(1)
    a.left = BinaryTree(2)
    a.left.left = BinaryTree(4)
    a.left.right = BinaryTree(5)

    a.right = BinaryTree(3)


# Iterator --> https://stackoverflow.com/questions/19151/build-a-basic-python-iterator#24377
# Amazing --> https://codereview.stackexchange.com/questions/183942/use-generator-to-do-inorder-traversal
# Very good --> http://thatmattbone.com/binary-tree-traversal-in-python-with-generators.html
# https://github.com/joowani/binarytree
# https://medium.com/the-renaissance-developer/learning-tree-data-structure-27c6bb363051
# https://www.geeksforgeeks.org/?p=2686
