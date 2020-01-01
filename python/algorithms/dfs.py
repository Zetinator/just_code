"""implementation of the depth first search algorithm
https://www.youtube.com/watch?v=AfSk24UTFS8
https://en.wikipedia.org/wiki/Graph_traversal#Depth-first_search
"""
from data_structures import graph

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
def dfs(graph: graph.Graph, start, end) -> list:
    """returns when the first path is found from the start node to the end node
    creates the topological order first and the the path to node: end is retrived
    """
    # set-up
    parents = {start: None}
    def r(graph, current_node, found=False):
        for node in graph.neighbors(current_node):
            if found: return True
            if node not in parents:
                parents[node] = current_node
                if node == end: return True
                found = r(graph, node)
        return found
    if not r(graph, start): raise ValueError(f'node: {end} not reachable from node: {start}')
    return retrieve_path(parents, end)
