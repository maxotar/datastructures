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
    a = BinaryTree(1)
    a.left = BinaryTree(2)
    a.left.left = BinaryTree(4)
    a.left.right = BinaryTree(5)
    a.right = BinaryTree(3)
    assert list(a.preorder()) == [1, 2, 4, 5, 3]


def test_inorder():
    a = BinaryTree(1)
    a.left = BinaryTree(2)
    a.left.left = BinaryTree(4)
    a.left.right = BinaryTree(5)
    a.right = BinaryTree(3)
    assert list(a.inorder()) == [4, 2, 5, 1, 3]


def test_postorder():
    a = BinaryTree(1)
    a.left = BinaryTree(2)
    a.left.left = BinaryTree(4)
    a.left.right = BinaryTree(5)
    a.right = BinaryTree(3)
    assert list(a.postorder()) == [4, 5, 2, 3, 1]


def test_levelorder():
    a = BinaryTree(1)
    a.left = BinaryTree(2)
    a.left.left = BinaryTree(4)
    a.left.right = BinaryTree(5)
    a.right = BinaryTree(3)
    a.right.left = BinaryTree(6)
    a.right.right = BinaryTree(7)
    assert list(a.levelorder()) == [1, 2, 3, 4, 5, 6, 7]


def test_levelordernested():
    a = BinaryTree(1)
    a.left = BinaryTree(2)
    a.left.left = BinaryTree(4)
    a.left.right = BinaryTree(5)
    a.right = BinaryTree(3)
    a.right.left = BinaryTree(6)
    a.right.right = BinaryTree(7)
    assert list(a.levelordernested()) == [[1], [2, 3], [4, 5, 6, 7]]
