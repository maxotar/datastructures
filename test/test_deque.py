from deque import Deque


def test_size():
    myDQ = Deque()
    myDQ.addRear(1)
    assert myDQ.size() == 1


def test_addFront_removeFront():
    myDQ = Deque()
    myDQ.addFront(1)
    myDQ.addFront(2)
    myDQ.addFront(3)
    myDQ.addFront(4)
    assert myDQ.removeFront() == 4


def test_addRear_removeRear():
    myDQ = Deque()
    myDQ.addRear(1)
    myDQ.addRear(2)
    myDQ.addRear(3)
    myDQ.addRear(4)
    assert myDQ.removeRear() == 4


def test_isEmpty():
    myDQ = Deque()
    assert myDQ.isEmpty()
