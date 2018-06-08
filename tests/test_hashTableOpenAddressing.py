from datastructures.hashTableOpenAddressing import HashTableOpenAddressing
import pytest


def test_init():
    myht = HashTableOpenAddressing()
    assert len(myht._buckets) == myht.MINSIZE


def test_init_some_initial_values():
    myht = HashTableOpenAddressing(one='dog', two='cat')
    assert myht.get('one') == 'dog'
    assert myht.get('two') == 'cat'


def test_init_too_many_values():
    myht = HashTableOpenAddressing(one='dog', two='cat',
                                   three='horse', four='monkey',
                                   five='goat', six='waffle',
                                   seven='strawberry', eight='mouse',
                                   nine='rat')
    assert myht.get('one') == 'dog'
    assert myht.get('two') == 'cat'
    assert myht.get('nine') == 'rat'


def test_insert_one():
    myht = HashTableOpenAddressing()
    myht.insert('one', 'dog')
    assert myht.get('one') == 'dog'


def test_invalid_key():
    with pytest.raises(KeyError):
        myht = HashTableOpenAddressing()
        myht['one'] = 'dog'
        myht['two']


def test_bracket_method():
    myht = HashTableOpenAddressing()
    myht['one'] = 'dog'
    assert myht['one'] == 'dog'


def test_overwrite():
    myht = HashTableOpenAddressing()
    myht['one'] = 'dog'
    assert myht['one'] == 'dog'
    myht['one'] = 'cat'
    assert myht['one'] == 'cat'


def test_utilization():
    myht = HashTableOpenAddressing()
    assert myht.utilization == 0
    myht['one'] = 'dog'
    assert myht.utilization == 1 / len(myht._buckets)
