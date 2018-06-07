from datastructures.node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def isEmpty(self):
        return not self.head

    def add(self, item):
        newNode = Node(item)
        newNode.next = self.head
        self.head = newNode
        if not self.tail:
            self.tail = newNode
        self.length += 1

    def size(self):
        return self.length

    def search(self, item):
        cur = self.head
        while cur:
            if cur.data == item:
                return True
            else:
                cur = cur.next
        return False

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

    def append(self, item):
        newNode = Node(item)
        if not self.tail:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1

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

    def insert(self, pos=None, item=None):
        if pos is None or item is None:
            raise ValueError('invalid arguments')
        if not isinstance(pos, int):
            raise TypeError('integer argument expected')
        if pos < -self.length:
            self.add(item)
            return
        if pos > self.length - 1:
            self.append(item)
            return

        if pos < 0:
            pos = self.length + pos

        index = 0
        prev = None
        cur = self.head
        while cur:
            if index == pos:
                newNode = Node(item)
                if prev:
                    prev.next = newNode
                else:
                    self.head = newNode
                newNode.next = cur
                self.length += 1
                break
            else:
                prev = cur
                cur = cur.next
                index += 1

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

    def reverse(self):
        if self.head:
            if self.head.next:
                prev = None
                cur = self.head
                self.tail = self.head
                while cur:
                    next = cur.next
                    cur.next = prev
                    prev = cur
                    cur = next
                self.head = prev
