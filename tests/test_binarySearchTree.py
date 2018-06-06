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
    root.insert(0)
    assert root.data == 1
    assert root.left.data == 0
    assert root.right.data == 2
    assert list(root.levelorder()) == [1, 0, 2]


def test_search():
    root = BinarySearchTree(2)
    root.insert(0)
    root.insert(1)
    root.insert(4)
    assert root.right.data == 4
    assert root.search(4)
    assert not root.search(3)


def test_minValue():
    root = BinarySearchTree(2)
    root.insert(0)
    root.insert(-1)
    root.insert(1)
    root.insert(4)
    assert root.minValue() == -1


def test_maxValue():
    root = BinarySearchTree(2)
    root.insert(0)
    root.insert(-1)
    root.insert(1)
    root.insert(4)
    assert root.maxValue() == 4


def test_minNode():
    root = BinarySearchTree(2)
    root.insert(0)
    root.insert(-1)
    root.insert(1)
    root.insert(4)
    assert root.minNode().data == -1


def test_maxNode():
    root = BinarySearchTree(2)
    root.insert(0)
    root.insert(-1)
    root.insert(1)
    root.insert(4)
    assert root.maxNode().data == 4


def test_preorder():
    root = BinarySearchTree(5)
    root.insert(2)
    root.insert(-4)
    root.insert(18)
    root.insert(3)
    assert list(root.preorder()) == [5, 2, -4, 3, 18]


def test_inorder():
    root = BinarySearchTree(5)
    root.insert(2)
    root.insert(-4)
    root.insert(18)
    root.insert(3)
    assert list(root.inorder()) == [-4, 2, 3, 5, 18]


def test_postorder():
    root = BinarySearchTree(5)
    root.insert(2)
    root.insert(-4)
    root.insert(18)
    root.insert(3)
    assert list(root.postorder()) == [-4, 3, 2, 18, 5]


def test_levelorder():
    root = BinarySearchTree(5)
    root.insert(2)
    root.insert(-4)
    root.insert(18)
    root.insert(3)
    assert list(root.levelorder()) == [5, 2, 18, -4, 3]


def test_levelordernested():
    root = BinarySearchTree(5)
    root.insert(2)
    root.insert(-4)
    root.insert(18)
    root.insert(3)
    assert list(root.levelordernested()) == [[5], [2, 18], [-4, 3]]


def test_toList():
    root = BinarySearchTree(5)
    root.insert(2)
    root.insert(-4)
    root.insert(18)
    root.insert(3)
    assert root.toList() == [5, 2, 18, -4, 3]


def test___str__():
    root = BinarySearchTree(5)
    root.insert(2)
    root.insert(-4)
    root.insert(18)
    root.insert(3)
    assert root.__str__() == str([5, 2, 18, -4, 3])


def test_remove_nochildren():
    root = BinarySearchTree(4)
    root.insert(2)
    root.insert(6)
    root.insert(1)
    root.insert(3)
    root.insert(5)
    root.insert(7)
    assert list(root.levelorder()) == [4, 2, 6, 1, 3, 5, 7]
    root.remove(7)
    assert list(root.levelordernested()) == [[4], [2, 6], [1, 3, 5]]


def test_remove_onechild():
    root = BinarySearchTree(4)
    root.insert(2)
    root.insert(6)
    root.insert(1)
    root.insert(3)
    root.insert(5)
    root.insert(7)
    assert list(root.levelorder()) == [4, 2, 6, 1, 3, 5, 7]
    root.remove(7)
    root.remove(6)
    assert list(root.levelordernested()) == [[4], [2, 5], [1, 3]]


def test_remove_twochildren():
    root = BinarySearchTree(4)
    root.insert(2)
    root.insert(6)
    root.insert(1)
    root.insert(3)
    root.insert(5)
    root.insert(7)
    assert list(root.levelorder()) == [4, 2, 6, 1, 3, 5, 7]
    root.remove(7)
    root.remove(6)
    root.remove(2)
    assert list(root.levelordernested()) == [[4], [3, 5], [1]]


def test_remove_root():
    root = BinarySearchTree(4)
    root.insert(2)
    root.insert(6)
    root.insert(1)
    root.insert(3)
    root.insert(5)
    root.insert(7)
    assert list(root.levelorder()) == [4, 2, 6, 1, 3, 5, 7]
    root.remove(4)
    assert list(root.levelordernested()) == [[5], [2, 6], [1, 3, 7]]


def test_height():
    root = BinarySearchTree(4)
    root.insert(2)
    root.insert(6)
    root.insert(1)
    root.insert(3)
    root.insert(5)
    root.insert(7)
    assert list(root.levelorder()) == [4, 2, 6, 1, 3, 5, 7]
    assert root.height() == 3
