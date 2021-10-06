from dataclasses import dataclass

@dataclass
class path:
    def __init__(self, adj):
        self.path = []
        self.adj = adj

    def distance(self):
        distance = 0
        for i in range(0, len(self.path) - 1):
            f = self.path[i]
            t = self.path[i+1]
            distance += self.adj[f][t]
        return distance 

    def add_vertex(self, v):
        self.path.append(v)
    
    def last(self):
        return self.path[-1]
