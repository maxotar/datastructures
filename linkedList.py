from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        newNode = Node(item)
        newNode.setNext(self.head)
        self.head = newNode
        if self.tail == None:
            self.tail = newNode

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        # Check if we are at head
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
            if current.getNext() == None:
                self.tail = previous

    def append(self, item):
        newNode = Node(item)
        if self.tail == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.setNext(newNode)
            self.tail = newNode

    def index(self, item):
        pass

    def insert(self, pos, item):
        pass

    def pop(self, pos=-1):
        pass

    def toList(self):
        outputList = []
        current = self.head

        while current != None:
            outputList.append(current.getData())
            current = current.getNext()

        return outputList


if __name__ == "__main__":
    mylist = LinkedList()
    mylist.add(1)
    mylist.add(2)
    mylist.add(3)
    mylist.append(0)

    print("\n Let's convert to a python list.")
    print(mylist.toList())
