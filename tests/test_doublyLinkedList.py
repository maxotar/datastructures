from datastructures.doublyLinkedList import DoublyLinkedList


def test_add():
    mylist = DoublyLinkedList()
    mylist.add(1)
    mylist.add(2)
    mylist.add(3)
    mylist.add(4)
    assert mylist.search(1)
    assert mylist.search(2)
    assert mylist.search(3)
    assert mylist.search(4)
    assert not mylist.search(5)
    assert len(mylist) == 4


def test_append():
    mylist = DoublyLinkedList()
    mylist.append(1)
    mylist.append(2)
    mylist.append(3)
    mylist.add(4)
    assert mylist.search(1)
    assert mylist.search(2)
    assert mylist.search(3)
    assert mylist.search(4)
    assert not mylist.search(5)
    assert len(mylist) == 4


def test_remove():
    mylist = DoublyLinkedList()
    assert len(mylist) == 0
    mylist.add(1)
    mylist.append(2)
    assert mylist.search(2)
    assert mylist.search(1)
    assert not mylist.remove(3)
    assert mylist.remove(2)
    assert mylist.remove(1)
    assert not mylist.search(2)
    assert not mylist.search(1)
