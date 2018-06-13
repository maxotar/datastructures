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
