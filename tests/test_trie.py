from datastructures.trie import Trie
import pytest


def test_creation():
    mytrie = Trie()
    mytrie.insert('test', 3)
    mytrie.insert('hello', 9)
    assert mytrie.get('hello') == 9
    assert mytrie.get('test') == 3
    with pytest.raises(KeyError):
        mytrie.get('cat')


def test_overwrite():
    mytrie = Trie()
    mytrie.insert('test', 3)
    mytrie.insert('test', 4)
    assert mytrie.get('test') == 4


def test_remove():
    mytrie = Trie()
    mytrie.insert('test', 3)
    mytrie.insert('again', 2)
    mytrie.remove('test')
    with pytest.raises(KeyError):
        mytrie.get('test')
