import Heap, Graph
from random import randrange

heap = Heap.min_heap()

for i in range(1, 7):
    random = randrange(1, 10)
    heap.add(random)

print(heap.heap)

graph = [[0, 3, 2],
         [2, 0, 4],
         [4, 0, 1]]

path = [2, 0, 1]

def distance(path):
    distance = 0
    for i in range(0, len(path) - 1):
        f = path[i]
        t = path[i+1]
        distance += graph[f][t]
    return distance 

print(distance(path))
