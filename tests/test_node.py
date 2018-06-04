from datastructures.node import Node


def test_getData_setData():
    myNode = Node(3)
    assert myNode.data == 3


def test_getNext_setNext():
    myNode = Node(5)
    secondNode = Node(7)
    myNode.next = secondNode
    assert myNode.next.data == 7
