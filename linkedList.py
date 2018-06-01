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
        cur = self.head
        count = 0
        while cur != None:
            count += 1
            cur = cur.getNext()
        return count

    def search(self, item):
        cur = self.head
        found = False
        while cur != None and not found:
            if cur.getData() == item:
                found = True
            else:
                cur = cur.getNext()
        return found

    def remove(self, item):
        cur = self.head
        prev = None
        found = False
        while not found:
            if cur.getData() == item:
                found = True
            else:
                prev = cur
                cur = cur.getNext()
        # Check if we are at head
        if prev == None:
            self.head = cur.getNext()
        else:
            prev.setNext(cur.getNext())
            if cur.getNext() == None:
                self.tail = prev

    def append(self, item):
        newNode = Node(item)
        if self.tail == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.setNext(newNode)
            self.tail = newNode

    def index(self, item):
        cur = self.head
        count = 0
        index = -1
        while cur != None:
            if cur.getData() == item:
                index = count
                break
            else:
                cur = cur.getNext()
                count += 1
        return index

    def insert(self, pos, item):
        if pos == 0:
            self.add(item)
        elif pos == -1:
            self.append(item)
        else:
            index = 0
            prev = None
            cur = self.head
            while cur != None:
                if index == pos:
                    newNode = Node(item)
                    prev.setNext(newNode)
                    newNode.setNext(cur)
                    break
                else:
                    prev = cur
                    cur = cur.getNext()
                    index += 1

    def pop(self, pos=-1):
        pass

    def toList(self):
        outputList = []
        cur = self.head

        while cur != None:
            outputList.append(cur.getData())
            cur = cur.getNext()

        return outputList


if __name__ == "__main__":
    mylist = LinkedList()
    mylist.add(1)
    mylist.add(2)
    mylist.add(3)
    mylist.append(0)

    print("\n Let's convert to a python list.")
    print(mylist.toList())
