"""implementation of the Single-Source Shortest Paths  with dynamic programming
https://www.youtube.com/watch?v=GazC3A4OQTE
https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
"""
from data_structures import wgraph
from functools import lru_cache

def sssp(graph, start, end):
    d = dict().fromkeys(graph.nodes, float('inf'))

    @lru_cache(maxsize=1000)
    def r(c_node, end, c_distance):
        print(f'c_node: {c_node}, c_distance: {c_distance}')
        # already visited with less effort
        if d[c_node] < c_distance: return (float('inf'), c_node)
        d[c_node] = c_distance
        # match
        if c_node == end: return (c_distance, c_node)
        # keep looking ;)
        return min([(float('inf'), c_node)]+[r(_next, end, c_distance + graph.weight(c_node, _next))
                        for _next in graph.neighbors(c_node)])
    return r(start, end, 0)

graph = {0: [(1, 1),(2, 7)],
          1 : [(3, 9), (5, 15)],
          2 : [(4, 4)],
          3 : [(4, 10), (5, 5)],
          4 : [(5, 3)],
          5 : []
        }
graph = wgraph.WGraph(graph)
