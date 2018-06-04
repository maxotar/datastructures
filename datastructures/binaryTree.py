class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insertLeft(self, newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.left = self.left
            self.left = tree

    def insertRight(self, newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.right = self.right
            self.right = tree

    def preorder(self):
        print(self.data)

        if self.left:
            self.left.preorder()

        if self.right:
            self.right.preorder()

    def inorder(self):
        if self.left:
            self.left.inorder()

        print(self.data)

        if self.right:
            self.right.inorder()

    def postorder(self):
        if self.left:
            self.left.postorder()

        if self.right:
            self.right.postorder()

        print(self.data)


if __name__ == "__main__":
    a = BinaryTree(0)
    a.left = BinaryTree(1)
    a.left.left = BinaryTree(2)
    a.left.right = BinaryTree(3)

    a.right = BinaryTree(4)
    a.right.left = BinaryTree(5)
    a.right.right = BinaryTree(6)

    a.preorder()


# https://github.com/joowani/binarytree
# https://medium.com/the-renaissance-developer/learning-tree-data-structure-27c6bb363051
# https://www.geeksforgeeks.org/?p=2686
