"""implementation of the kruskal's algorithm
https://visualgo.net/en/mst
https://www.youtube.com/watch?v=GazC3A4OQTE
https://en.wikipedia.org/wiki/Kruskal%27s_algorithm
"""
from data_structures import wgraph
from data_structures import disjoint_set


def kruskal(graph: wgraph.WGraph) -> list:
    """returns min spanning tree in the given graph
    """
    # set-up
    cycle_detector, edges = disjoint_set.DJS(), set()
    q = sorted(graph.edges, key=lambda x: graph.weight(x[0], x[1]))
    for edge in q:
        # no cycles allowed...
        if cycle_detector.same(*edge): continue
        edges.add(edge)
        cycle_detector.union(*edge)
    return edges
