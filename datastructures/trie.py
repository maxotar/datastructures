class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.key = None
        self.value = None

    def hasChildren(self):
        return any(self.children)

    def isLeafNode(self):
        return self.value is not None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def _charToIndex(self, ch):
        return ord(ch) - ord('a')

    def insert(self, key, value):
        cur = self.root
        for ch in key:
            i_next = self._charToIndex(ch)
            if not cur.children[i_next]:
                cur.children[i_next] = TrieNode()
            cur = cur.children[i_next]
        cur.key = key
        cur.value = value
        return True

    def get(self, key):
        cur = self.root
        for ch in key:
            i_next = self._charToIndex(ch)
            try:
                cur = cur.children[i_next]
            except:
                raise KeyError('invalid key')
        return cur.value

    def _removeHelper(self, cur, key, level):
        try:
            if cur.key == key:  # Base Case. Found the leaf node
                cur.value = None
                if cur.hasChildren():
                    return False  # No, we didn't delete this node
                else:  # No children
                    cur = None
                    return True  # Yes, we did delete this node
            else:  # recursive case
                index = self._charToIndex(key[level])
                if self._removeHelper(cur.children[index], key, level+1):
                    cur.children[index] = None
                    # Recursion if not a leaf and no children
                    return not cur.isLeafNode() and not cur.hasChildren()
        except:
            raise KeyError('invalid key')

    def remove(self, key=None):
        try:
            length = len(key)
            if length > 0:
                self._removeHelper(self.root, key, 0)
        except:
            KeyError('invalid key')
