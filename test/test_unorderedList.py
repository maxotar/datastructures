from unorderedList import UnorderedList


def test_isEmpty():
    myList = UnorderedList()
    assert myList.isEmpty()


def test_add_search():
    myList = UnorderedList()
    myList.add(1)
    myList.add(2)
    myList.add(3)
    myList.add(5)
    myList.add(6)
    assert myList.search(6)
    assert not myList.search(4)


def test_size():
    myList = UnorderedList()
    myList.add(1)
    myList.add(2)
    assert myList.size() == 2


def test_remove():
    myList = UnorderedList()
    myList.add(1)
    myList.add(2)
    myList.add(3)
    myList.remove(2)
    assert not myList.search(2)


def test_append():
    myList = UnorderedList()
    myList.add(1)
    myList.add(2)
    myList.add(3)
    myList.append(0)
    assert myList.search(0)
