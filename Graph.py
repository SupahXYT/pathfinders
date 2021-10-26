from random import randrange

class path_heap:
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
        parent = (i-1) >> 1

        while current > 0:
            if self.heap[current].distance() < self.heap[parent].distance():
                self.heap[current], self.heap[parent] = self.heap[parent], self.heap[current]
            current = parent
            parent = (current-1) >> 1

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
 
class path:
    def __init__(self, graph):
        self.path = []
        self.graph = graph

    def distance(self):
        if self.path[-1] == None:
            return -1
        distance = 0
        for i in range(len(self.path) - 1):
            f = i
            t = i+1
            distance += self.graph[self.path[f]][self.path[t]]
        return distance 

    def add_vertex(self, v):
        self.path.append(v)
    
    def last(self):
        return self.path[-1]

class graph:
    def __init__(self, v):
        self.graph = [[0 for i in range(v)] for j in range(v)]

    def randomize_dumb(self):
        for i in range(0, len(self.graph)):
            for j in range(0, len(self.graph)):
                if i == j:
                    self.graph[i][j] = 0
                else:
                    random = randrange(1, 10)
                    self.graph[i][j] = random

    def randomize_depth_first(self):
        visited = []
        pass

    def shortest_path(self, start, end):
        paths = path_heap()
        visited = []
        current = start

        startingpath = path(self.graph)
        startingpath.add_vertex(start)
        paths.add(startingpath)
        # While not travsersed all possible paths
        while len(paths.heap) > 0:
            local_path = paths.remove()
            current = local_path.last()
            if current == end:
                return local_path
            # for every other node
            for i in range(len(self.graph)):
                # check if neighbor
                if self.graph[current][i] > 0 and not self.visited(i):
                    p = path(self.graph)
                    p.path = [i for i in local_path.path]
                    p.add_vertex(i)
                    paths.add(p)
            visited.append(current)

        fin = path(self.graph)
        fin.add_vertex(None)
        return fin

    def visited(self, vertex):
        for i in range(0, len(self.graph)):
            if self.graph[i] == vertex:
                return True
        return False
 
