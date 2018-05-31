from stack import Stack


def test_isEmpty_empty_stack():
    myStack = Stack()
    assert myStack.isEmpty()


def test_isEmpty_non_empty_stack():
    myStack = Stack()
    myStack.push(1)
    assert not myStack.isEmpty()


def test_pop():
    myStack = Stack()
    myStack.push(2)
    assert myStack.pop() == 2


def test_peek():
    myStack = Stack()
    myStack.push(3)
    myStack.push(4)
    assert myStack.peek() == 4


def test_size():
    myStack = Stack()
    myStack.push(3)
    myStack.push(4)
    assert myStack.size() == 2
