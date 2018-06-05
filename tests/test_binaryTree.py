from datastructures.binaryTree import BinaryTree


def test_creation():
    root = BinaryTree(7)
    assert root.data == 7
    assert root.left is None
    assert root.right is None


def test_insertion():
    root = BinaryTree(0)
    root.insertRight(2)
    root.insertRight(1)
    assert root.right.data == 1
    assert root.right.right.data == 2


def test_preorder():
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.right = BinaryTree(3)
    assert list(root.preorder()) == [1, 2, 4, 5, 3]


def test_inorder():
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.right = BinaryTree(3)
    assert list(root.inorder()) == [4, 2, 5, 1, 3]


def test_postorder():
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.right = BinaryTree(3)
    assert list(root.postorder()) == [4, 5, 2, 3, 1]


def test_levelorder():
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.right = BinaryTree(3)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)
    assert list(root.levelorder()) == [1, 2, 3, 4, 5, 6, 7]


def test_levelordernested():
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.right = BinaryTree(3)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)
    assert list(root.levelordernested()) == [[1], [2, 3], [4, 5, 6, 7]]
