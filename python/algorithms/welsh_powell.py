"""implementation of the welsh powell's algorithm
a greedy algorithm for couloring graphs...
https://en.wikipedia.org/wiki/Graph_coloring
https://en.wikipedia.org/wiki/Graph_coloring#CITEREFWelshPowell1967
"""
from data_structures import ugraph

def welsh_powell(g: ugraph.UGraph) -> list:
    """returns a color_map: color_map[node] -> color
    the rules are simple... no adjacent nodes can have the same color
    """
    # set-up
    color_map = {}
    # order nodes by degree
    uncolored = sorted(g.nodes, key= lambda node: -len(g.neighbors(node)))
    for current_node in uncolored:
        # colors already used with the neighbors...
        avoid = set([color_map.get(node) for node in g.neighbors(current_node)])
        # select next availible color
        color_map[current_node] = next(c for c in range(len(g.nodes)) if c not in avoid)
    return color_map
