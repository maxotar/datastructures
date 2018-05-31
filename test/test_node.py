from node import Node


def test_getData_setData():
    myNode = Node(3)
    assert myNode.getData() == 3


def test_getNext_setNext():
    myNode = Node(5)
    secondNode = Node(7)
    myNode.setNext(secondNode)
    assert myNode.getNext().getData() == 7
