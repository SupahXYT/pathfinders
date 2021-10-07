import Heap, Path
from random import randrange
from math import inf

heap = Heap.min_heap()

for i in range(1, 7):
    random = randrange(1, 10)
    heap.add(random)

# print(heap.heap)

def new_graph(v):
    # I really wish I could do 
    # Path graph[v][v];
    graph = [[0 for i in range(v)] for j in range(v)]
    for i in range(0, v):
        for j in range(0, v):
            random = randrange(1, 4)
            graph[i][j] = random
            if i == j:
                graph[i][j] = 0

    return graph

# graph = new_graph(5)

graph = [[0, 3, 1, 1],
         [3, 0, inf, 3],
         [2, inf, 0, inf],
         [1, 3, inf, 0]]

# graph = [[0, inf, inf],
#          [inf, 0, 2],
#          [inf, 2, 0]]

# given two vertices in the graph G this function returns 
# the shortest path between those two vertices with a path object

print(graph)

# returns path object containing shortest path if found 
# or returns new path instance representing no path
def dijkstra(start, end):
    heap = Heap.path_heap()
    visited = []
    current = start

    startingpath = Path.path(graph)
    startingpath.add_vertex(start)
    heap.add(startingpath)
    # While not dead end
    while len(heap.heap) > 0:
        path = heap.remove()
        current = path.last()
        if current == end:
            return path
        # for every other node
        for i in range(len(graph)):
            # check if neighbor
            if graph[current][i] > 0 and graph[current][i] < inf and not contains(visited, i):
                p = Path.path(graph)
                p.path = [i for i in path.path]
                p.add_vertex(i)
                heap.add(p)
        visited.append(current)

    fin = Path.path(graph)
    fin.add_vertex(None)
    return fin

def contains(list, n):
    for i in range(0, len(list)):
        if list[i] == n:
            return True
    return False
        
f, t = 2, 1
shortest = dijkstra(f, t)
print(f'shortest path from {f} to {t}: {shortest.path}')
print(f'distance: {shortest.distance()}')

