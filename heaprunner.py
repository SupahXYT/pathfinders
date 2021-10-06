import Heap, Path
from random import randrange

heap = Heap.min_heap()

for i in range(1, 7):
    random = randrange(1, 10)
    heap.add(random)

print(heap.heap)

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

graph = new_graph(3)

# given two vertices in the graph G this function returns 
# the shortest path between those two vertices with a path object

print(graph)

def dijkstra(start, end):
    heap = Heap.path_heap()
    visited = []
    current = start

    startingpath = Path.path(graph)
    startingpath.add_vertex(start)
    heap.add(startingpath)
    
    # while 
    while not (current == end):
        path = heap.remove()
        current = path.last()
        if current == end:
            return path.path
        # for every other node
        for i in range(len(graph)):
            # check if neighbor
            if graph[current][i] > 0 and not contains(visited, i):
                print(i)
                print(path.path)
                p = Path.path(graph)
                p.path = [i for i in path.path]
                p.add_vertex(i)
                heap.add(p)
                visited.append(current)

    return heap

def contains(list, n):
    for i in range(0, len(list)):
        if list[i] == n:
            return True
    return False
        

shortest = dijkstra(1, 2)
print(f'path: {shortest.tostring()}')

# def distance(path):
#     distance = 0
#     for i in range(0, len(path) - 1):
#         f = path[i]
#         t = path[i+1]
#         distance += graph[f][t]
#     return distance 
