"""implementation of the tarjan's algorithm
https://visualgo.net/en/dfsbfs
https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm
"""
from data_structures import ugraph

def tarjan(g: ugraph.UGraph) -> list:
    """returns the strongly connected nodes in the given graph
    """
    # set-up
    indexes, low_i = {}, {}
    # connected components, and the strongly connected components
    cc_stack, scc = [], []
    def r(current_node):
        tarjan.i += 1
        indexes[current_node], low_i[current_node] = tarjan.i, tarjan.i
        cc_stack.append(current_node)
        for neighbor in g.neighbors(current_node):
            # no revisiting...
            if neighbor not in indexes: r(neighbor)
            # update low_indexes...
            low_i[current_node] = min(low_i[current_node], low_i[neighbor])
        # are you root?
        if low_i[current_node] == indexes[current_node]:
            # pop visited components until we get the root
            tmp = []
            while cc_stack:
                tmp.append(cc_stack.pop())
                if tmp[-1] == current_node: break
            scc.append(tmp)
    # make sure to visit all the nodes...
    for start in g.nodes:
        tarjan.i = 0
        if start not in indexes: r(start)
    return scc
