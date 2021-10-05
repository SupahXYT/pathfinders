import Heap
from random import randrange

heap = Heap.heap()

for i in range(1, 7):
    random = randrange(1, 10)
    heap.add(random)

print(heap.heap)
