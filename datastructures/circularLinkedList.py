class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

        if self.tail:
            self.tail.next = self.head
        else:
            self.tail = self.head

    def search(self, data):
        cur = self.head
        while cur:
            if cur.data == data:
                return True
            elif cur.next == self.head:  # Didn't find it
                break
            else:
                cur = cur.next
        return False

    def remove(self, data):
        prev = None
        cur = self.head
        while cur:
            if cur.data == data:
                if prev:  # Not first element
                    if cur == self.tail:  # Last element
                        self.tail = prev
                        self.tail.next = self.head
                    else:  # Middle element
                        prev.next = cur.next
                else:  # First element
                    if cur == cur.next:  # Only one element
                        self.head = None
                        self.tail = None
                    else:  # Not the only element
                        self.head = cur.next
                        self.tail.next = self.head
                return True
            elif cur.next == self.head:  # Didn't find it
                break
            else:
                prev = cur
                cur = cur.next
        return False
