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


def test_keys():
    myht = HashTableOpenAddressing()
    myht['one'] = 'dog'
    myht['two'] = 'cat'
    assert 'two' in myht.keys
    assert 'one' in myht.keys


def test_values():
    myht = HashTableOpenAddressing()
    myht['one'] = 'dog'
    myht['two'] = 'cat'
    assert 'dog' in myht.values
    assert 'cat' in myht.values


def test_delete():
    with pytest.raises(KeyError):
        myht = HashTableOpenAddressing()
        myht['one'] = 'dog'
        myht['two'] = 'cat'
        myht.delete('two')
        myht['two']


def test_delete_2():
    myht = HashTableOpenAddressing()
    myht['one'] = 'dog'
    myht['two'] = 'cat'
    del myht['two']
    assert 'two' not in myht.keys


def test_everything():
    myht = HashTableOpenAddressing()
    myht['1'] = 'one'
    myht['2'] = 'two'
    myht['3'] = 'three'
    myht['4'] = 'four'
    myht['5'] = 'five'
    myht['6'] = 'six'
    myht['7'] = 'seven'
    myht['8'] = 'eight'
    myht['9'] = 'nine'
    assert len(myht._buckets) == 32
    del myht['1']
    del myht['2']
    del myht['3']
    del myht['4']
    del myht['5']
    del myht['6']
    del myht['7']
    del myht['8']
    assert len(myht._buckets) == 8
