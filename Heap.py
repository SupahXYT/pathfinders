
# Array implementation of binary heap (min)
class heap():
    def __init__(self):
        self.heap = []

    def remove(self):
        head = self.heap.pop(0)
        self.heapdown()
        return head

    def add(self, data):
        i = 0; parent = int((i-1)/2)
        # while self.heap[parent] < data:
        leftchild = i*2+1
        rightchild = i*2+2

        print(f'{parent}, {leftchild}, {rightchild}')
            # i += 1



    def heapdown(self):
        pass

    def tostring(self):
        pass

