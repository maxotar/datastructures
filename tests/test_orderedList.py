from datastructures.orderedList import OrderedList
import pytest


class Test_utility:
    def test_isEmpty(self):
        mylist = OrderedList()
        assert mylist.isEmpty()

    def test_search(self):
        mylist = OrderedList()
        mylist.add(1)
        mylist.add(2)
        mylist.add(3)
        mylist.add(5)
        mylist.add(6)
        assert mylist.search(6)
        assert not mylist.search(4)

    def test_size(self):
        mylist = OrderedList()
        mylist.add(1)
        mylist.add(2)
        assert mylist.size() == 2

    def test_toList(self):
        mylist = OrderedList()
        mylist.add(1)
        mylist.add(2)
        mylist.add(3)
        assert mylist.toList() == [1, 2, 3]

    def test_clear(self):
        mylist = OrderedList()
        mylist.add(1)
        mylist.add(2)
        mylist.add(3)
        mylist.clear()
        assert mylist.size() == 0
        assert mylist.isEmpty()
        assert mylist.toList() == []

    def test_index(self):
        mylist = OrderedList()
        mylist.add(1)
        mylist.add(2)
        mylist.add(3)
        assert mylist.index(3) == 2
        assert mylist.index(2) == 1
        assert mylist.index(1) == 0
        assert mylist.index(4) == -1


class Test_remove:
    def test_empty_list(self):
        mylist = OrderedList()
        mylist.remove(1)
        assert mylist.isEmpty()

    def test_one_item(self):
        mylist = OrderedList()
        mylist.add(3)
        mylist.remove(3)
        assert mylist.isEmpty()

    def test_many_duplicates(self):
        mylist = OrderedList()
        mylist.add(3)
        mylist.add(3)
        mylist.add(3)
        mylist.remove(3)
        assert mylist.toList() == [3, 3]

    def test_remove_first(self):
        mylist = OrderedList()
        mylist.add(1)
        mylist.add(2)
        mylist.add(3)
        mylist.remove(3)
        assert mylist.toList() == [1, 2]

    def test_remove_last(self):
        mylist = OrderedList()
        mylist.add(1)
        mylist.add(2)
        mylist.add(3)
        mylist.remove(1)
        assert mylist.toList() == [2, 3]


class Test_pop:
    def test_empty_list(self):
        with pytest.raises(IndexError):
            mylist = OrderedList()
            mylist.pop()

    def test_non_integer_pos(self):
        with pytest.raises(TypeError):
            mylist = OrderedList()
            mylist.add(3)
            mylist.pop(.4)

    def test_one_item_first(self):
        mylist = OrderedList()
        mylist.add(2)
        assert mylist.pop(0) == 2
        assert mylist.isEmpty()

    def test_index_out_of_range(self):
        with pytest.raises(IndexError):
            mylist = OrderedList()
            mylist.add(2)
            mylist.pop(100)

    def test_index_out_of_range_low(self):
        with pytest.raises(IndexError):
            mylist = OrderedList()
            mylist.add(2)
            mylist.pop(-100)

    def test_one_item_last(self):
        mylist = OrderedList()
        mylist.add(2)
        assert mylist.pop(-1) == 2
        assert mylist.isEmpty()

    def test_many_items_first(self):
        mylist = OrderedList()
        mylist.add(1)
        mylist.add(2)
        mylist.add(3)
        assert mylist.pop(0) == 1
        assert mylist.size() == 2

    def test_many_items_last(self):
        mylist = OrderedList()
        mylist.add(1)
        mylist.add(2)
        mylist.add(3)
        assert mylist.pop(-1) == 3
        assert mylist.size() == 2

    def test_many_items_middle(self):
        mylist = OrderedList()
        mylist.add(1)
        mylist.add(2)
        mylist.add(3)
        assert mylist.pop(-2) == 2
        assert mylist.size() == 2
