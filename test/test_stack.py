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


def test_toList():
    myStack = Stack()
    myStack.push(3)
    myStack.push(4)
    assert myStack.toList() == [3, 4]


def test_clear():
    myStack = Stack()
    myStack.push(3)
    myStack.push(4)
    myStack.clear()
    assert myStack.size() == 0
    assert myStack.isEmpty()
    assert myStack.toList() == []
