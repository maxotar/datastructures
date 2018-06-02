from datastructures.node import Node


class OrderedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def isEmpty(self):
        return self.head == None

    def size(self):
        return self.length

    def add(self, item):
        prev = None
        cur = self.head
        stop = False
        while cur is not None and not stop:
            if cur.getData() > item:
                stop = True
            else:
                prev = cur
                cur = cur.getNext()

        newNode = Node(item)
        if prev is None:
            self.head = newNode
        else:
            prev.setNext(newNode)
        newNode.setNext(cur)
        self.length += 1

    def remove(self, item):
        if self.length > 0:
            prev = None
            cur = self.head
            while cur is not None:
                if cur.getData() == item:
                    if self.length == 1:
                        self.head = None
                        self.tail = None
                    elif prev == None:
                        self.head = cur.getNext()
                    else:
                        prev.setNext(cur.getNext())
                        if cur.getNext() == None:
                            self.tail = prev
                    self.length -= 1
                    return
                else:
                    prev = cur
                    cur = cur.getNext()

    def search(self, item):
        cur = self.head
        while cur is not None:
            if cur.getData() == item:
                return True
            if cur.getData() > item:
                return False
            else:
                cur = cur.getNext()
        return False

    def index(self, item):
        cur = self.head
        count = 0
        index = -1
        while cur is not None:
            if cur.getData() == item:
                index = count
                break
            else:
                cur = cur.getNext()
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
        while cur is not None:
            if index == pos:
                if prev == None and cur.getNext() == None:
                    self.head = None
                    self.tail = None
                elif cur.getNext() == None:
                    self.tail = prev
                    self.tail.setNext(None)
                elif prev == None:
                    self.head = cur.getNext()
                else:
                    prev.setNext(cur.getNext())

                self.length -= 1
                return cur.getData()
            else:
                prev = cur
                cur = cur.getNext()
                index += 1

    def toList(self):
        outputList = []
        cur = self.head

        while cur is not None:
            outputList.append(cur.getData())
            cur = cur.getNext()

        return outputList

    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        return str(self.toList())
