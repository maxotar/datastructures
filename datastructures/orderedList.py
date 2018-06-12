class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class OrderedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def isEmpty(self):
        return not self.head

    def size(self):
        return self.length

    def add(self, item):
        prev = None
        cur = self.head
        stop = False
        while cur and not stop:
            if cur.data > item:
                stop = True
            else:
                prev = cur
                cur = cur.next

        newNode = Node(item)
        if not prev:
            self.head = newNode
        else:
            prev.next = newNode
        newNode.next = cur
        self.length += 1

    def remove(self, item):
        if self.length > 0:
            prev = None
            cur = self.head
            while cur:
                if cur.data == item:
                    if self.length == 1:
                        self.head = None
                        self.tail = None
                    elif not prev:
                        self.head = cur.next
                    else:
                        prev.next = cur.next
                        if not cur.next:
                            self.tail = prev
                    self.length -= 1
                    return
                else:
                    prev = cur
                    cur = cur.next

    def search(self, item):
        cur = self.head
        while cur:
            if cur.data == item:
                return True
            if cur.data > item:
                return False
            else:
                cur = cur.next
        return False

    def index(self, item):
        cur = self.head
        count = 0
        index = -1
        while cur:
            if cur.data == item:
                index = count
                break
            else:
                cur = cur.next
                count += 1
        return index

    def pop(self, pos=-1):
        if self.length == 0:
            raise IndexError('pop from empty list')
        if not isinstance(pos, int):
            raise TypeError('integer argument expected')
        if pos > self.length - 1 or pos < -self.length:
            raise IndexError('index out of range')

        if pos < 0:
            pos = self.length + pos

        index = 0
        prev = None
        cur = self.head
        while cur:
            if index == pos:
                if not prev and not cur.next:
                    self.head = None
                    self.tail = None
                elif not cur.next:
                    self.tail = prev
                    self.tail.next = None
                elif not prev:
                    self.head = cur.next
                else:
                    prev.next = cur.next

                self.length -= 1
                return cur.data
            else:
                prev = cur
                cur = cur.next
                index += 1

    def toList(self):
        outputList = []
        cur = self.head

        while cur:
            outputList.append(cur.data)
            cur = cur.next

        return outputList

    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        return str(self.toList())
