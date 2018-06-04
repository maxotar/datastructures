from datastructures.node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        newNode = Node(item)
        newNode.next = self.head
        self.head = newNode
        if self.tail == None:
            self.tail = newNode
        self.length += 1

    def size(self):
        return self.length

    def search(self, item):
        cur = self.head
        while cur is not None:
            if cur.data == item:
                return True
            else:
                cur = cur.next
        return False

    def remove(self, item):
        if self.length > 0:
            prev = None
            cur = self.head
            while cur is not None:
                if cur.data == item:
                    if self.length == 1:
                        self.head = None
                        self.tail = None
                    elif prev == None:
                        self.head = cur.next
                    else:
                        prev.next = cur.next
                        if cur.next == None:
                            self.tail = prev
                    self.length -= 1
                    return
                else:
                    prev = cur
                    cur = cur.next

    def append(self, item):
        newNode = Node(item)
        if self.tail == None:
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
        while cur is not None:
            if cur.data == item:
                index = count
                break
            else:
                cur = cur.next
                count += 1
        return index

    def insert(self, pos=None, item=None):
        if pos == None or item == None:
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
        while cur is not None:
            if index == pos:
                newNode = Node(item)
                if prev is not None:
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
        while cur is not None:
            if index == pos:
                if prev == None and cur.next == None:
                    self.head = None
                    self.tail = None
                elif cur.next == None:
                    self.tail = prev
                    self.tail.next = None
                elif prev == None:
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

        while cur is not None:
            outputList.append(cur.data)
            cur = cur.next

        return outputList

    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        return str(self.toList())