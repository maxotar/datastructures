class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add(self, data):
        newNode = Node(data)
        if self.tail:
            newNode.next = self.head
            self.head.prev = newNode
        else:
            self.tail = newNode
        self.head = newNode
        self.length += 1

    def search(self, data):
        cur = self.head
        while cur:
            if cur.data == data:
                return True
            else:
                cur = cur.next
        return False

    def append(self, data):
        newNode = Node(data)
        if self.head:
            newNode.prev = self.tail
            self.tail.next = newNode
        else:
            self.head = newNode
        self.tail = newNode
        self.length += 1

    def remove(self, data):
        prev = None
        cur = self.head
        while cur:
            if cur.data == data:  # Found the element
                if self.length == 0:  # No elements
                    return False
                elif self.length == 1:  # One element
                    self.head = None
                    self.tail = None
                    self.length -= 1
                    return True
                elif prev is None:  # First element
                    self.head = cur.next
                    self.head = None
                    self.length -= 1
                    return True
                elif cur == self.tail:  # Last element
                    self.tail = prev
                    self.tail.next = None
                    self.length -= 1
                    return True
            else:
                prev = cur
                cur = cur.next
        return False  # Didn't find the element

    def __len__(self):
        return self.length
