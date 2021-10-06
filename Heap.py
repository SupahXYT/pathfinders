
# Array implementation of max heap 
class max_heap():
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
        for i in range(0, len(self.heap)):
            self.heapup(i)

    def tostring(self):
        return str(self.heap)

class min_heap():
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
            if self.heap[current] < self.heap[parent]:
                self.heap[current], self.heap[parent] = self.heap[parent], self.heap[current]
            current = parent
            parent = int((current-1)/2)

    def heapdown(self):
        for i in range(0, len(self.heap)):
            self.heapup(i)

class path_heap():
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
            if self.heap[current].distance() < self.heap[parent].distance():
                self.heap[current], self.heap[parent] = self.heap[parent], self.heap[current]
            current = parent
            parent = int((current-1)/2)

    def heapdown(self):
        for i in range(0, len(self.heap)):
            self.heapup(i)

    def tostring(self):
        string = "["
        for i in range(0, len(self.heap)):
            string += str(self.heap[i].path)
            string += str(self.heap[i].distance())

        string += "]"
        return string
            
            

        

