class BinaryHeap():
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self.percUp(self.size)

    def percUp(self, i):
        while i // 2 > 0:
            # Parent index is always = i // 1
            if self.heap[i] < self.heap[i // 2]:
                self.heap[i // 2], self.heap[i] = self.heap[i], self.heap[i // 2]
            i = i // 2

    def percDown(self, i):
        while i * 2 <= self.size:
            mc = self.minChild(i)
            if self.heap[i] > self.heap[mc]:
                self.heap[i], self.heap[mc] = self.heap[mc], self.heap[i]
            i = mc

    def minChild(self, i):
        # Child index is always 2*parent + 1
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.heap[i * 2] < self.heap[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def popMin(self):
        if self.size > 0:
            minValue = self.heap[1]
            poppedValue = self.heap.pop()
            self.size -= 1
            if self.size > 0:
                self.heap[1] = poppedValue
                self.percDown(1)
            return minValue
        else:
            raise IndexError('heap is empty')

    def buildFrom(self, input):
        i = len(input) // 2
        self.size = len(input)
        self.heap = [0] + input
        while i > 0:
            self.percDown(i)
            i -= 1
