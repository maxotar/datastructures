class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def pop(self):
        return self.items.pop()

    def clear(self):
        self.items = []

    def toList(self):
        return self.items

    def __str__(self):
        return str(self.toList())
