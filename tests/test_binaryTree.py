from datastructures.binaryTree import BinaryTree


def test_creation():
    root = BinaryTree(7)
    assert root.data == 7
    assert root.left == None
    assert root.right == None


def test_insertion():
    root = BinaryTree(0)
    root.insertRight(2)
    root.insertRight(1)
    assert root.right.data == 1
    assert root.right.right.data == 2
