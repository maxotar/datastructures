from unorderedList import UnorderedList


def test_isEmpty():
    myUL = UnorderedList()
    assert myUL.isEmpty()


def test_add_search():
    myUL = UnorderedList()
    myUL.add(1)
    myUL.add(2)
    myUL.add(3)
    myUL.add(5)
    myUL.add(6)
    assert myUL.search(6)
    #assert myUL.search(4)


def test_size():
    myUL = UnorderedList()
    myUL.add(1)
    myUL.add(2)
    assert myUL.size() == 2
