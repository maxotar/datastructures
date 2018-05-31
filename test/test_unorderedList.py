from unorderedList import UnorderedList


def test_isEmpty():
    mylist = UnorderedList()
    assert mylist.isEmpty()


def test_add_search():
    mylist = UnorderedList()
    mylist.add(1)
    mylist.add(2)
    mylist.add(3)
    mylist.add(5)
    mylist.add(6)
    assert mylist.search(6)
    assert not mylist.search(4)


def test_size():
    mylist = UnorderedList()
    mylist.add(1)
    mylist.add(2)
    assert mylist.size() == 2


def test_remove():
    mylist = UnorderedList()
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
    mylist = UnorderedList()
    mylist.append(0)
    assert mylist.toList() == [0]
    mylist.add(1)
    assert mylist.toList() == [1, 0]
    mylist.append(5)
    assert mylist.toList() == [1, 0, 5]


def test_tolist():
    mylist = UnorderedList()
    mylist.add(1)
    mylist.add(2)
    mylist.add(3)
    assert mylist.toList() == [3, 2, 1]
