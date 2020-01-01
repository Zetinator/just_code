"""implementation of the prim's algorithm
https://visualgo.net/en/mst
https://www.youtube.com/watch?v=GazC3A4OQTE
https://en.wikipedia.org/wiki/Prim%27s_algorithm
"""
from data_structures import wgraph
from data_structures import min_heap


def prim(graph: wgraph.WGraph) -> list:
    """returns min spanning tree in the given graph
    """
    # special case: empty graph
    if not graph: return
    # set-up
    c_node = graph.nodes[0]
    heap = min_heap.Heap([(graph.weight(c_node,i), i, c_node) for i in graph.neighbors(c_node)])
    nodes, edges = {c_node}, set()
    min_weight = 0
    while heap and len(nodes) <= len(graph.nodes):
        # get next min edge and add the node and edge to 'nodes' and 'edges'
        _, c_node, parent = heap.pop()
        # no revisiting...
        if c_node in nodes: continue
        # update global stats
        min_weight += graph.weight(parent, c_node)
        edges.add((parent, c_node))
        nodes.add(c_node)
        # let the action take place
        for neighbor in graph.neighbors(c_node):
            # relax a little, I'm glad I inspire you but Stan, why are you so mad?
            heap.push((graph.weight(neighbor, c_node), neighbor, c_node))
    return edges
