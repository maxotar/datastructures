from datastructures.queue import Queue


def test_isEmpty():
    myQ = Queue()
    assert myQ.isEmpty()


def test_enqueue_dequeue():
    myQ = Queue()
    myQ.enqueue(2)
    assert myQ.dequeue() == 2


def test_size():
    myQ = Queue()
    myQ.enqueue(2)
    assert myQ.size() == 1


def test_toList():
    myQ = Queue()
    myQ.enqueue(3)
    myQ.enqueue(4)
    assert myQ.toList() == [4, 3]


def test_clear():
    myQ = Queue()
    myQ.enqueue(3)
    myQ.enqueue(4)
    myQ.clear()
    assert myQ.size() == 0
    assert myQ.isEmpty()
    assert myQ.toList() == []
