
# Array implementation of binary heap (min)
class heap():
    def __init__(self):
        self.heap = []

    def remove(self):
        head = self.heap.pop(0)
        self.heapdown()
        return head

    def add(self, data):
        self.heap.append(data)
        self.heapup(len(self.heap) - 1)

    def heapup(self, i):
        current = i
        parent = int((i-1)/2)

        while current > 0:
            if self.heap[current] > self.heap[parent]:
                self.heap[current], self.heap[parent] = self.heap[parent], self.heap[current]
            current = parent
            parent = int((current-1)/2)

    def heapdown(self):
        pass

    def tostring(self):
        return self.heap

