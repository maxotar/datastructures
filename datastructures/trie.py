class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.key = None
        self.value = None


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
