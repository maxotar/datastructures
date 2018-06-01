from linkedList import LinkedList


def test_isEmpty():
    mylist = LinkedList()
    assert mylist.isEmpty()


def test_add_search():
    mylist = LinkedList()
    mylist.add(1)
    mylist.add(2)
    mylist.add(3)
    mylist.add(5)
    mylist.add(6)
    assert mylist.search(6)
    assert not mylist.search(4)


def test_size():
    mylist = LinkedList()
    mylist.add(1)
    mylist.add(2)
    assert mylist.size() == 2


def test_remove():
    mylist = LinkedList()
    mylist.add(1)
    mylist.add(2)
    mylist.add(3)
    mylist.remove(1)
    assert mylist.toList() == [3, 2]
    mylist.remove(3)
    assert mylist.toList() == [2]
    mylist.remove(2)
    assert mylist.toList() == []


def test_append():
    mylist = LinkedList()
    mylist.append(0)
    assert mylist.toList() == [0]
    mylist.add(1)
    assert mylist.toList() == [1, 0]
    mylist.append(5)
    assert mylist.toList() == [1, 0, 5]


def test_tolist():
    mylist = LinkedList()
    mylist.add(1)
    mylist.add(2)
    mylist.add(3)
    assert mylist.toList() == [3, 2, 1]


def test_index():
    mylist = LinkedList()
    mylist.add(1)
    mylist.add(2)
    mylist.add(3)
    assert mylist.index(3) == 0
    assert mylist.index(2) == 1
    assert mylist.index(1) == 2
    assert mylist.index(4) == -1


def test_insert():
    mylist = LinkedList()
    mylist.add(1)
    mylist.add(2)
    mylist.add(3)
    mylist.insert(0, 4)
    assert mylist.toList() == [4, 3, 2, 1]
    mylist.insert(-1, 0)
    assert mylist.toList() == [4, 3, 2, 1, 0]
    mylist.insert(1, 3.5)
    assert mylist.toList() == [4, 3.5, 3, 2, 1, 0]
    mylist.insert(3, 2.5)
    assert mylist.toList() == [4, 3.5, 3, 2.5, 2, 1, 0]
    mylist.insert(300, 2.5)
    assert mylist.toList() == [4, 3.5, 3, 2.5, 2, 1, 0]
