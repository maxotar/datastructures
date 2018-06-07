from datastructures.binaryHeap import BinaryHeap
import pytest


def test_init():
    myheap = BinaryHeap()
    assert myheap.heap == [0]
    assert myheap.size == 0


def test_insert():
    myheap = BinaryHeap()
    myheap.insert(1)
    myheap.insert(11)
    myheap.insert(12)
    myheap.insert(13)
    myheap.insert(14)
    myheap.insert(5)
    myheap.insert(4)
    assert myheap.heap == [0, 1, 11, 4, 13, 14, 12, 5]
    assert myheap.size == 7


def test_buildFrom():
    myheap = BinaryHeap()
    myheap.buildFrom([9, 6, 5, 2, 3])
    assert myheap.heap == [0, 2, 3, 5, 6,  9]


def test_popMin():
    myheap = BinaryHeap()
    myheap.buildFrom([9, 6, 5, 2, 3])
    myheap.popMin()
    assert myheap.heap == [0, 3, 6, 5, 9]
    myheap.popMin()
    assert myheap.heap == [0, 5, 6, 9]
    myheap.popMin()
    assert myheap.heap == [0, 6, 9]
    myheap.popMin()
    assert myheap.heap == [0, 9]
    myheap.popMin()
    assert myheap.heap == [0]


def test_popMin_emptyHeap():
    with pytest.raises(IndexError):
        myheap = BinaryHeap()
        myheap.popMin()
