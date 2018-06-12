from datastructures.hashTableSeparateChaining import HashTableSeparateChaining
import pytest


def test_creation():
    myht = HashTableSeparateChaining(one='dog', two='cat',
                                     three='horse', four='monkey',
                                     five='goat', six='waffle',
                                     seven='strawberry', eight='mouse',
                                     nine='rat')
    assert myht.get('one') == 'dog'
    assert myht.get('two') == 'cat'
    assert myht.get('nine') == 'rat'


def test_insert_one():
    myht = HashTableSeparateChaining()
    myht.insert('one', 'dog')
    assert myht.get('one') == 'dog'


def test_invalid_key():
    with pytest.raises(KeyError):
        myht = HashTableSeparateChaining()
        myht['one'] = 'dog'
        myht['two']


def test_bracket_method():
    myht = HashTableSeparateChaining()
    myht['one'] = 'dog'
    assert myht['one'] == 'dog'


def test_overwrite():
    myht = HashTableSeparateChaining()
    myht['one'] = 'dog'
    assert myht['one'] == 'dog'
    myht['one'] = 'cat'
    assert myht['one'] == 'cat'


def test_delete():
    with pytest.raises(KeyError):
        myht = HashTableSeparateChaining()
        myht['one'] = 'dog'
        myht['two'] = 'cat'
        myht.delete('two')
        myht['two']


def test_delete_2():
    myht = HashTableSeparateChaining()
    myht['one'] = 'dog'
    myht['two'] = 'cat'
    myht['three'] = 'horse'
    del myht['two']
    assert myht['one'] == 'dog'
    myht['three'] = 'horse'
    del myht['one']
    del myht['three']
