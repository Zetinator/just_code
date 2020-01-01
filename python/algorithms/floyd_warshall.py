"""implementation of the floyd's algorithm
https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
"""
from data_structures import wgraph

def floyd_warshall(g: wgraph.WGraph) -> list:
    """returns the shortest path between all the nodes in the wgraph in O(N**3)
    good for dense graphs... for sparse ones use johnson's algorithm
    """
    # set all unknowns pairs (u,v) to inf, and source -> source to 0's
    distances = [[float('inf')]*len(graph.nodes) for line in graph.nodes]
    weight = lambda node: graph.weight(*node) if graph.weight(*node)!=None else float('inf')
    for u, line in enumerate(graph.nodes):
        for v, e in enumerate(graph.nodes):
            distances[u][v] = weight((u, v))
            if u == v: distances[u][v] = 0
    # the longest possible simple path is V-1 nodes long...
    for k in graph.nodes[1:]:
        for u in graph.nodes:
            for v in graph.nodes:
                delta = distances[u][k] + distances[k][v]
                distances[u][v] = min(distances[u][v], delta)
    # the diagonal must be 0's otherwise, cycles otherwise...
    n = len(distances)
    if any([distances[i][j] for i in range(n) for j in range(n) if i== j]):
        raise ValueError('negative cycle detected...')
    return distances

graph = {0: [(1, 9),(2, 75)],
      1 : [(0, 9), (2, 95), (3, 19), (4, 15)],
      2 : [(0, 75), (1,95), (3, 51)],
      3 : [(1, 19), (2, 51), (4, 31)],
      4 : [(1, 15),(3, 31)],
    }
graph = wgraph.WGraph(graph)
res = floyd_warshall(graph)
for line in res: print(line)
