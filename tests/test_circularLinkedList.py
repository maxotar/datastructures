from datastructures.circularLinkedList import CircularLinkedList


def test_search():
    mylist = CircularLinkedList()
    assert not mylist.search(1)
    mylist.add(1)
    assert mylist.search(1)
    mylist.add(2)
    assert mylist.search(1)
    assert mylist.search(2)
    mylist.add(3)
    assert mylist.search(1)
    assert mylist.search(2)
    assert mylist.search(3)


def test_remove():
    mylist = CircularLinkedList()
    mylist.add(1)
    mylist.add(2)
    mylist.add(3)
    mylist.add(4)
    mylist.add(5)

    # Remove first
    mylist.remove(5)
    assert not mylist.search(5)

    # Remove last
    mylist.remove(1)
    assert not mylist.search(1)

    # Remove middle
    mylist.remove(3)
    assert not mylist.search(3)

    # Remove all
    mylist.remove(2)
    assert not mylist.search(2)
    mylist.remove(4)
    assert not mylist.search(4)
