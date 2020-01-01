"""implementation of the floyd's algorithm
https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
"""
from data_structures import wgraph

def retrieve_path(parents: dict, start, end):
    """returns the path from start to the given end
    """
    parents, path = parents[start][end], []
    while end != None:
        path.append(end)
        end = parents[end]
    path.reverse()
    return path

def floyd_warshall(graph: wgraph.WGraph) -> list:
    """returns the shortest path between all the nodes in the wgraph in O(N**3)
    good for dense graphs... for sparse ones use johnson's algorithm, or dijkstra
    this version retrieves the min 'distance' matrix and paths matrix 'parents'
    """
    # set all unknowns pairs (u,v) to inf, and source -> source to 0's
    distances = [[float('inf')]*len(graph.nodes) for line in graph.nodes]
    parents = {}
    weight = lambda node: graph.weight(*node) if graph.weight(*node)!=None else float('inf')
    for u, line in enumerate(graph.nodes):
        parents.setdefault(u, {})
        for v, e in enumerate(graph.nodes):
            distances[u][v] = weight((u, v))
            parents[u].setdefault(v, {u: None, v: u})
            if u == v: distances[u][v] = 0
    # the longest possible simple path is V-1 nodes long...
    for k in graph.nodes[1:]:
        for u in graph.nodes:
            for v in graph.nodes:
                delta = distances[u][k] + distances[k][v]
                if delta < distances[u][v]:
                    distances[u][v] = delta
                    parents[u][v][v] = k
                    parents[u][v][k] = u
                distances[u][v] = min(distances[u][v], delta)
    # the diagonal must be 0's, otherwise we have cycles...
    n = len(distances)
    if any([distances[i][j] for i in range(n) for j in range(n) if i== j]):
        raise ValueError('negative cycle detected...')
    return distances, parents
