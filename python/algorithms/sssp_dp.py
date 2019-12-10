"""implementation of the Single-Source Shortest Paths with dynamic programming
https://www.youtube.com/watch?v=GazC3A4OQTE
https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
"""
from data_structures import wgraph
from functools import lru_cache

def sssp_dp(graph, start, end):
    """returns the shortest path between start and end using dynamic programming
    """
    d = dict().fromkeys(graph.nodes, float('inf'))

    @lru_cache(maxsize=1000)
    def r(c_node, end, c_distance):
        # already visited with less effort, skip...
        if d[c_node] < c_distance: return (float('inf'), c_node)
        d[c_node] = c_distance
        # match
        if c_node == end: return (c_distance, c_node)
        # keep looking ;)
        res = min([(float('inf'), c_node)]+[r(_next, end, c_distance + graph.weight(c_node, _next))
                        for _next in graph.neighbors(c_node)])
        return res + (c_node,)
    min_distance, *path = r(start, end, 0)
    path.reverse()
    return path
