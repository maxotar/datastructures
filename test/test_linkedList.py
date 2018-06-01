from linkedList import LinkedList
import pytest


class Test_utility:
    def test_isEmpty(self):
        mylist = LinkedList()
        assert mylist.isEmpty()

    def test_search(self):
        mylist = LinkedList()
        mylist.add(1)
        mylist.add(2)
        mylist.add(3)
        mylist.add(5)
        mylist.add(6)
        assert mylist.search(6)
        assert not mylist.search(4)

    def test_size(self):
        mylist = LinkedList()
        mylist.add(1)
        mylist.add(2)
        assert mylist.size() == 2

    def test_append(self):
        mylist = LinkedList()
        mylist.append(0)
        assert mylist.toList() == [0]
        mylist.add(1)
        assert mylist.toList() == [1, 0]
        mylist.append(5)
        assert mylist.toList() == [1, 0, 5]

    def test_toList(self):
        mylist = LinkedList()
        mylist.add(1)
        mylist.add(2)
        mylist.add(3)
        assert mylist.toList() == [3, 2, 1]

    def test_clear(self):
        mylist = LinkedList()
        mylist.add(1)
        mylist.add(2)
        mylist.add(3)
        mylist.clear()
        assert mylist.size() == 0
        assert mylist.isEmpty()
        assert mylist.toList() == []

    def test_index(self):
        mylist = LinkedList()
        mylist.add(1)
        mylist.add(2)
        mylist.add(3)
        assert mylist.index(3) == 0
        assert mylist.index(2) == 1
        assert mylist.index(1) == 2
        assert mylist.index(4) == -1


class Test_insert:
    def test_missing_arg(self):
        with pytest.raises(ValueError):
            mylist = LinkedList()
            mylist.insert(1)

    def test_non_integer_index(self):
        with pytest.raises(TypeError):
            mylist = LinkedList()
            mylist.insert(2.2, 1)

    def test_index_low(self):
        mylist = LinkedList()
        mylist.add(2)
        mylist.insert(-100, 1)
        assert mylist.toList() == [1, 2]
        assert mylist.size() == 2

    def test_index_high(self):
        mylist = LinkedList()
        mylist.add(2)
        mylist.insert(100, 1)
        assert mylist.toList() == [2, 1]
        assert mylist.size() == 2

    def test_insert_front_empty(self):
        mylist = LinkedList()
        mylist.insert(0, 1)
        assert mylist.toList() == [1]
        assert mylist.size() == 1

    def test_insert_front_one(self):
        mylist = LinkedList()
        mylist.add(2)
        mylist.insert(0, 1)
        assert mylist.toList() == [1, 2]
        assert mylist.size() == 2

    def test_insert_front_full_list(self):
        mylist = LinkedList()
        mylist.add(2)
        mylist.add(3)
        mylist.add(4)
        mylist.insert(0, 1)
        assert mylist.toList() == [1, 4, 3, 2]
        assert mylist.size() == 4

    def test_insert_middle_full_list(self):
        mylist = LinkedList()
        mylist.add(1)
        mylist.add(2)
        mylist.add(3)
        mylist.add(4)
        mylist.insert(2, 17)
        assert mylist.toList() == [4, 3, 17, 2, 1]
        assert mylist.size() == 5

    def test_insert_back_empty(self):
        mylist = LinkedList()
        mylist.insert(-1, 1)
        assert mylist.toList() == [1]
        assert mylist.size() == 1

    def test_insert_back_one(self):
        mylist = LinkedList()
        mylist.add(2)
        mylist.insert(-1, 1)
        assert mylist.toList() == [1, 2]
        assert mylist.size() == 2

    def test_insert_back_full_list(self):
        mylist = LinkedList()
        mylist.add(2)
        mylist.add(3)
        mylist.add(4)
        mylist.add(5)
        mylist.insert(-3, 1)
        assert mylist.toList() == [5, 1, 4, 3, 2]
        assert mylist.size() == 5


class Test_remove:
    def test_empty_list(self):
        mylist = LinkedList()
        mylist.remove(1)
        assert mylist.isEmpty()

    def test_one_item(self):
        mylist = LinkedList()
        mylist.add(3)
        mylist.remove(3)
        assert mylist.isEmpty()

    def test_many_duplicates(self):
        mylist = LinkedList()
        mylist.add(3)
        mylist.add(3)
        mylist.add(3)
        mylist.remove(3)
        assert mylist.toList() == [3, 3]

    def test_remove_first(self):
        mylist = LinkedList()
        mylist.add(1)
        mylist.add(2)
        mylist.add(3)
        mylist.remove(3)
        assert mylist.toList() == [2, 1]

    def test_remove_last(self):
        mylist = LinkedList()
        mylist.add(1)
        mylist.add(2)
        mylist.add(3)
        mylist.remove(1)
        assert mylist.toList() == [3, 2]


class Test_pop:
    def test_empty_list(self):
        with pytest.raises(IndexError):
            mylist = LinkedList()
            mylist.pop()

    def test_non_integer_pos(self):
        with pytest.raises(TypeError):
            mylist = LinkedList()
            mylist.add(3)
            mylist.pop(.4)

    def test_one_item_first(self):
        mylist = LinkedList()
        mylist.add(2)
        assert mylist.pop(0) == 2
        assert mylist.isEmpty()

    def test_index_out_of_range(self):
        with pytest.raises(IndexError):
            mylist = LinkedList()
            mylist.add(2)
            mylist.pop(100)

    def test_index_out_of_range_low(self):
        with pytest.raises(IndexError):
            mylist = LinkedList()
            mylist.add(2)
            mylist.pop(-100)

    def test_one_item_last(self):
        mylist = LinkedList()
        mylist.add(2)
        assert mylist.pop(-1) == 2
        assert mylist.isEmpty()

    def test_many_items_first(self):
        mylist = LinkedList()
        mylist.add(1)
        mylist.add(2)
        mylist.add(3)
        assert mylist.pop(0) == 3
        assert mylist.size() == 2

    def test_many_items_last(self):
        mylist = LinkedList()
        mylist.add(1)
        mylist.add(2)
        mylist.add(3)
        assert mylist.pop(-1) == 1
        assert mylist.size() == 2

    def test_many_items_middle(self):
        mylist = LinkedList()
        mylist.add(1)
        mylist.add(2)
        mylist.add(3)
        assert mylist.pop(-2) == 2
        assert mylist.size() == 2
