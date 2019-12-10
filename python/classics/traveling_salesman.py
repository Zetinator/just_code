"""traveling sales man... oh the the classics
https://www.youtube.com/watch?v=MEz1J9wY2iM
https://en.wikipedia.org/wiki/Travelling_salesman_problem
"""
from data_structures import wgraph
from data_structures import bit_mask
from functools import lru_cache

def tsp(graph):
    """returns the shortest path between start and end using dynamic programming
    """
    possible_states = 2**len(graph.nodes)-1
    min_states= dict().fromkeys([i for i in range(possible_states+1)], float('inf'))

    @lru_cache(maxsize=1000)
    def r(start, c_node, state, c_distance):
        # already visited with less effort, skip...
        if min_states[state] <= c_distance: return (float('inf'),)
        min_states[state] = c_distance
        print(f'node: {c_node}, state: {bin(state)}, d: {c_distance}')
        # all visited --> return to start
        if state == possible_states:
            total_d = c_distance+graph.weight(c_node, start)
            min_states[state] = total_d
            return (total_d, c_node)
        # keep looking ;)
        to_visit = [(float('inf'),)]
        for _next in graph.neighbors(c_node):
            delta = c_distance + graph.weight(c_node, _next)
            to_visit.append(r(start, _next, bit_mask.set(state, _next), delta))
        res = min(to_visit)
        return res + (c_node,)

    res_srcs = []
    for start in graph.nodes:
        state = bit_mask.set(0, start)
        res_srcs.append(r(start, start, state, 0))
    min_distance, *path = min(res_srcs)
    path.reverse()
    print(f'all cities visited following: {path}, in {min_distance}')
    return path

# test
d_matrix = [[0, 24, 13, 13, 22],
            [24, 0, 22, 13, 13],
            [13, 22, 0, 19, 14],
            [13, 13, 19, 0, 19],
            [22, 13, 14, 19, 0]]
graph = wgraph.WGraph(d_matrix)
tsp(graph)
