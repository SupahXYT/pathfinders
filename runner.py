import Graph

a = Graph.graph(5)

a.randomize_dumb()
print(a.graph)
path = a.shortest_path(1, 4)
print(path.path)
print(path.distance())
