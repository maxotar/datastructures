from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        newNode = Node(item)
        newNode.setNext(self.head)
        self.head = newNode
        if self.tail == None:
            self.tail = newNode
        self.length += 1

    def size(self):
        return self.length

    def search(self, item):
        cur = self.head
        found = False
        while cur is not None and not found:
            if cur.getData() == item:
                found = True
            else:
                cur = cur.getNext()
        return found

    def remove(self, item):
        if self.length > 0:
            prev = None
            cur = self.head
            found = False
            while not found:
                if cur.getData() == item:
                    found = True
                else:
                    prev = cur
                    cur = cur.getNext()
            if found:
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

    def append(self, item):
        newNode = Node(item)
        if self.tail == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.setNext(newNode)
            self.tail = newNode
        self.length += 1

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

    def insert(self, pos=None, item=None):
        if pos == None or item == None:
            raise ValueError('invalid arguments')
        if not isinstance(pos, int):
            raise TypeError('integer argument expected')
        if pos > self.length - 1:
            raise IndexError('index out of range')
        if pos == 0:
            self.add(item)
            self.length += 1
        elif pos == -1:
            self.append(item)
            self.length += 1
        else:
            index = 0
            prev = None
            cur = self.head
            while cur is not None:
                if index == pos:
                    newNode = Node(item)
                    prev.setNext(newNode)
                    newNode.setNext(cur)
                    self.length += 1
                    break
                else:
                    prev = cur
                    cur = cur.getNext()
                    index += 1

    def pop(self, pos=-1):
        prev = None
        cur = self.head

        if cur == None:
            raise IndexError('pop from empty list')
        if not isinstance(pos, int):
            raise TypeError('integer argument expected')
        if pos > self.length - 1:
            raise IndexError('index out of range')
        if pos == -1:
            while cur.getNext() is not None:
                prev = cur
                cur = cur.getNext()
            if prev == None:
                self.head = None
                self.tail = None
            else:
                prev.setNext(None)
                self.tail = prev
            return cur.getData()
        else:
            index = 0
            while cur.getNext() is not None:
                if index == pos:
                    if prev == None and cur.getNext() == None:
                        self.head = cur.getNext()
                        self.tail = None
                    elif cur.getNext() == None:
                        self.tail = prev
                        self.tail.setNext(None)
                    elif prev == None:
                        self.head = cur.getNext()
                    else:
                        prev.setNext(cur.getNext())

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


# https://stackoverflow.com/questions/22284578/linked-list-in-python-append-index-insert-and-pop-functions-not-sure-with-c?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
