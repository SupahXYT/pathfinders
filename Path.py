from math import inf

class path:
    def __init__(self, adj):
        self.path = []
        self.adj = adj

    def distance(self):
        if self.path[-1] == None:
            return inf
        distance = 0
        for i in range(len(self.path) - 1):
            f = i
            t = i+1
            distance += self.adj[self.path[f]][self.path[t]]
        return distance 

    def add_vertex(self, v):
        self.path.append(v)
    
    def last(self):
        return self.path[-1]
