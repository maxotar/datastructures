class HashTableOpenAddressing:

    MINSIZE = 8

    def __init__(self, **initial_values):
        self._buckets = [None] * self.MINSIZE

        for k, v in initial_values.items():
            self.insert(k, v)

    def computeHash(self, key):
        myhash = hash(key)
        mymask = len(self._buckets) - 1
        myid = myhash & mymask
        return (myhash, myid)

    def get(self, key):
        _, myid = self.computeHash(key)
        bucketsChecked = 0
        while self._buckets[myid] and self._buckets[myid][1] != key:
            bucketsChecked += 1
            if bucketsChecked < len(self._buckets):
                myid = 0 if myid == len(self._buckets) - 1 else myid + 1
            else:
                break
        else:  # Run if the while condition EVER hits false
            return self._buckets[myid][2] if self._buckets[myid] else None
        raise KeyError('key does not exist')

    def insert(self, key, value):
        myhash, myid = self.computeHash(key)

        if not self._buckets[myid]:
            self._buckets[myid] = (myhash, key, value)
        else:
            bucketsChecked = 0
            while self._buckets[myid] and self._buckets[myid][1] != key:
                bucketsChecked += 1
                if bucketsChecked < len(self._buckets):
                    myid = 0 if myid == len(self._buckets) - 1 else myid + 1
                else:
                    break
            else:  # Run if the while condition EVER hits false
                self._buckets[myid] = (myhash, key, value)
                return
            raise IndexError('table is full')

    @property
    def utilization(self):
        try:
            return float(len(self)) / float(len(self._buckets))
        except ZeroDivisionError:
            return 0

    def _resize(self, newsize):
        self.size = newsize
        old_buckets = self._buckets
        self._buckets = [None] * newsize

        # Move all the old buckets to new table
        for bucket in [b for b in old_buckets if b]:
            self.insert(bucket[1], bucket[2])

    def __setitem__(self, key, val):
        self.insert(key, val)

    def __getitem__(self, key):
        val = self.get(key)
        if val:
            return val
        else:
            raise KeyError('key does not exist')

    def __len__(self):
        return len([x for x in self._buckets if x])

# http://kells.tj/blog/2015/04/26/pure-python-hashtable.html
# http://interactivepython.org/courselib/static/pythonds/SortSearch/Hashing.html
