class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newVal):
        self.data = newVal

    def setNext(self, newNext):
        self.next = newNext
