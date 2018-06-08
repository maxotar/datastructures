class HashTableOpenAddressing:
    TOMBSTONE = 'RIP'
    MINSIZE = 8

    def __init__(self, **initial_values):
        self._buckets = [() for _ in range(self.MINSIZE)]

        for k, v in initial_values.items():
            self.insert(k, v)

    def get(self, key):
        _, myid = self._computeHash(key)
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
        self._grow()

        myhash, myid = self._computeHash(key)
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

    def delete(self, key):
        _, myid = self._computeHash(key)
        if not self._buckets[myid]:
            self._buckets[myid] = self.TOMBSTONE
            self._shrink()
        else:
            bucketsChecked = 0
            while self._buckets[myid] and self._buckets[myid][1] != key:
                bucketsChecked += 1
                if bucketsChecked < len(self._buckets):
                    myid = 0 if myid == len(self._buckets) - 1 else myid + 1
                else:
                    break
            else:  # Run if the while condition EVER hits false
                self._buckets[myid] = self.TOMBSTONE
                self._shrink()
                return
            raise KeyError('key does not exist')

    @property
    def utilization(self):
        try:
            return float(len(self)) / float(len(self._buckets))
        except ZeroDivisionError:
            return 0

    @property
    def keys(self):
        items = [bucket[1] for bucket in self._buckets if bucket]
        return items

    @property
    def values(self):
        items = [bucket[2] for bucket in self._buckets if bucket]
        return items

    def _computeHash(self, key):
        myhash = hash(key)
        mymask = len(self._buckets) - 1
        myid = myhash & mymask
        return (myhash, myid)

    def _grow(self):
        if self.utilization >= 0.75:
            self._resize(len(self._buckets) * 4)

    def _shrink(self):
        if 0 < self.utilization <= 0.16 and len(self._buckets) > self.MINSIZE:
            self._resize(len(self._buckets) // 4)

    def _resize(self, newsize):
        old_buckets = self._buckets
        self._buckets = [() for _ in range(newsize)]

        # Move all the old buckets to new table
        for bucket in [b for b in old_buckets if b and b != self.TOMBSTONE]:
            self.insert(bucket[1], bucket[2])

    def __setitem__(self, key, val):
        self.insert(key, val)

    def __getitem__(self, key):
        val = self.get(key)
        if val:
            return val
        else:
            raise KeyError('key does not exist')

    def __delitem__(self, key):
        self.delete(key)

    def __len__(self):
        return len([b for b in self._buckets if b and b != self.TOMBSTONE])

    def __str__(self):
        return str(list(zip(self.keys, self.values)))

# http://kells.tj/blog/2015/04/26/pure-python-hashtable.html
# http://interactivepython.org/courselib/static/pythonds/SortSearch/Hashing.html
