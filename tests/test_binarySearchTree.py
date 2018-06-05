from datastructures.binarySearchTree import BinarySearchTree


def test_creation():
    root = BinarySearchTree(7)
    assert root.data == 7
    assert root.left is None
    assert root.right is None


def test_insertion():
    root = BinarySearchTree(1)
    root.insert(2)
    root.insert(0)
    assert root.data == 1
    assert root.left.data == 0
    assert root.right.data == 2


def test_search():
    root = BinarySearchTree(2)
    root.insert(0)
    root.insert(1)
    root.insert(4)
    assert root.right.data == 4
    assert root.search(4)
    assert not root.search(3)


def test_min():
    root = BinarySearchTree(2)
    root.insert(0)
    root.insert(-1)
    root.insert(1)
    root.insert(4)
    assert root.min() == -1


def test_max():
    root = BinarySearchTree(2)
    root.insert(0)
    root.insert(-1)
    root.insert(1)
    root.insert(4)
    assert root.max() == 4

# def test_preorder():
#     a = BinarySearchTree(1)
#     a.left = BinarySearchTree(2)
#     a.left.left = BinarySearchTree(4)
#     a.left.right = BinarySearchTree(5)
#     a.right = BinarySearchTree(3)
#     assert list(a.preorder()) == [1, 2, 4, 5, 3]


# def test_inorder():
#     a = BinarySearchTree(1)
#     a.left = BinarySearchTree(2)
#     a.left.left = BinarySearchTree(4)
#     a.left.right = BinarySearchTree(5)
#     a.right = BinarySearchTree(3)
#     assert list(a.inorder()) == [4, 2, 5, 1, 3]


# def test_postorder():
#     a = BinarySearchTree(1)
#     a.left = BinarySearchTree(2)
#     a.left.left = BinarySearchTree(4)
#     a.left.right = BinarySearchTree(5)
#     a.right = BinarySearchTree(3)
#     assert list(a.postorder()) == [4, 5, 2, 3, 1]


# def test_levelorder():
#     a = BinarySearchTree(1)
#     a.left = BinarySearchTree(2)
#     a.left.left = BinarySearchTree(4)
#     a.left.right = BinarySearchTree(5)
#     a.right = BinarySearchTree(3)
#     a.right.left = BinarySearchTree(6)
#     a.right.right = BinarySearchTree(7)
#     assert list(a.levelorder()) == [1, 2, 3, 4, 5, 6, 7]


# def test_levelordernested():
#     a = BinarySearchTree(1)
#     a.left = BinarySearchTree(2)
#     a.left.left = BinarySearchTree(4)
#     a.left.right = BinarySearchTree(5)
#     a.right = BinarySearchTree(3)
#     a.right.left = BinarySearchTree(6)
#     a.right.right = BinarySearchTree(7)
#     assert list(a.levelordernested()) == [[1], [2, 3], [4, 5, 6, 7]]
