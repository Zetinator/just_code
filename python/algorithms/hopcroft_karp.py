"""implementation of the Hopcroft-Karp's algorithm
computes the maximal cardinality bipartite matching on a graph

unfortunately this a is a work in progress, use the dinic's approach alreadt programmed

https://visualgo.net/en/matching
https://en.wikipedia.org/wiki/Hopcroft%E2%80%93Karp_algorithm
"""
from data_structures import ugraph

def hopcroft_karp(graph: ugraph.UGraph, U, V) -> int:
    """computes the maximal cardinality bipartite matching on a graph
    """
    # set-up
    matched = set()
    hopcroft_karp.maximal = 0
    # standard dfs
    def dfs(node):
        """alternates between unmatched/matched until a free vertex is found
        if no vertex can be found -> no more augmenting paths... we are done
        """
        parents = {}
        def r(node):
            for neighbors in graph.neighbors(node):
                if neighbor not in parents:
                    parents[neighbor] = node
                    # augment path
                    if neighbor not in matched and node in V:
                        hopcroft_karp.maximal += 1
                        return
                    r(neighbor)

        return r(node)
    # standard bfs
    def bfs(start):
        """standard bfs, with implicit queue
        modified to stop once the sink is been reached and increase the max flow
        """
        parents = {}
        frontier = [start]
        while frontier:
            _next = []
            for current_node in frontier:
                for node in graph.neighbors(current_node):
                    if node not in matched:
                        # if we crossed the U -> V we are done...
                        if node in V:
                            matched.add(node)
                            matched.add(current_node)
                            hopcroft_karp.maximal += 1
                            return
                        _next.append(node)
            frontier = _next
    for u in U: bfs(u)
    for u in [u for u in U if u not in matched]: dfs(u)
    return hopcroft_karp.maximal


# test
graph = {0: [(1,5), (2,8), (3,3), (4,3), (5,7), (9,7)],
        1: [(9,4)],
        2: [(9,9)],
        3: [(6,1)],
        4: [(7,4)],
        5: [(8,6)],
        6: [(9,1)],
        7: [(9,6)],
        8: [(9,5)],
        }
# ford flukerson killer...
graph = {0: [(2,8), (1,8)],
        1: [(3,8)],
        2: [(3,8), (1,1)],
        }
# final case...
graph = {0: [(2,5), (3,3)],
        1: [(4,4)],
        2: [(4,3), (1,3), (3,3)],
        3: [(1,5)],
        }
graph = ugraph.UGraph(graph)
