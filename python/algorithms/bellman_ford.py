"""implementation of the bellman-ford algorithm
https://visualgo.net/en/sssp
https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm
"""
from data_structures import wgraph

def retrieve_path(parents: dict, node):
    """returns the path from start to the given end
    """
    path = []
    while node != None:
        path.append(node)
        node = parents[node]
    path.reverse()
    return path

# stop once end from start is found
def bellman_ford(graph: wgraph.WGraph, start, end) -> list:
    """returns the shortest paths from the single source to all the reachable nodes
    ...also detects negative cycles
    """
    # set-up
    parents = {start: None}
    distances = dict().fromkeys(graph.nodes, float('inf'))
    distances[start] = 0
    # the largest s-path will be at most V-1 long
    for node in graph.nodes[1:]:
        for edge in graph.edges:
            u, v = edge
            delta = graph.weight(u, v) + distances[u]
            if distances[v] > delta:
                distances[v], parents[v] = delta, u
    # detect cycles...
    for edge in graph.edges:
        u, v = edge
        delta = graph.weight(u, v) + distances[u]
        # if a path gets updated, we have cycles...
        if distances[v] > delta: raise ValueError(f'negative cycle detected...')
    return retrieve_path(parents, end)
