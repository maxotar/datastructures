from queue import Queue


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
