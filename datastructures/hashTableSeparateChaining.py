class HashTableSeparateChaining:
    SIZE = 128

    def __init__(self, **initial_values):
        self._buckets = [None] * self.SIZE
        for key, value in initial_values.items():
            self.insert(key, value)

    def insert(self, key, value):
        _, myid = self._computeHash(key)
        myList = self._buckets[myid]
        if myList:
            myNode = myList.nodeFromKey(key)
            if myNode:
                myNode.value = value
            else:
                myList.add(key, value)
        else:
            myList = KeyValueLinkedList()
            myList.add(key, value)
            self._buckets[myid] = myList

    def get(self, key):
        _, myid = self._computeHash(key)
        myList = self._buckets[myid]
        if myList:
            myNode = myList.nodeFromKey(key)
            if myNode:
                return myNode.value
        raise KeyError('invalid key')

    def delete(self, key):
        _, myid = self._computeHash(key)
        myList = self._buckets[myid]
        if myList:
            myList.delete(key)

    def _computeHash(self, key):
        myhash = hash(key)
        mymask = len(self._buckets) - 1
        myid = myhash & mymask
        return (myhash, myid)

    def __setitem__(self, key, value):
        self.insert(key, value)

    def __getitem__(self, key):
        value = self.get(key)
        if value:
            return value
        else:
            raise KeyError('key does not exist')

    def __delitem__(self, key):
        self.delete(key)


class KeyValueNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class KeyValueLinkedList:
    def __init__(self):
        self.head = None

    def add(self, key, value):
        newNode = KeyValueNode(key, value)
        newNode.next = self.head
        self.head = newNode

    def nodeFromKey(self, key):
        cur = self.head
        while cur:
            if cur.key == key:
                return cur
            else:
                cur = cur.next
        return None

    def delete(self, key):
        prev = None
        cur = self.head
        while cur:
            if cur.key == key:
                if prev:
                    prev.next = cur.next
                else:
                    if cur.next:
                        self.head = cur.next
                    else:
                        self.head = None
                return
            else:
                prev = cur
                cur = cur.next
        raise KeyError('invalid key')

# https://www.interviewbreeze.com/learn/hash-table-implementation/
