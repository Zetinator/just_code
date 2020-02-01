"""implementation of the breadth first search algorithm
https://www.youtube.com/watch?v=s-CYnVz-uh4
https://en.wikipedia.org/wiki/Breadth-first_search
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

def bfs(graph: graph.Graph, start, end) -> list:
    """returns when the first path is found from the start node to the end node
    """
    # special case: start = end
    if start == end: return start
    # set-up
    levels = {start: 0}
    parents = {start: None}
    level = 1
    front = [start]  # this is the current frontier being explored
    while front:
        _next = []  # will be the next frontier
        for current_node in front:  # iterate over the nodes in the current frontier
            for neighbor in graph.neighbors(current_node):  # build the next frontier
                # no revisiting
                if neighbor not in levels:
                    levels[neighbor] = level
                    parents[neighbor] = current_node
                    # match
                    if neighbor == end: return retrieve_path(parents, end)
                    _next.append(neighbor)
        front = _next
        level += 1
    raise ValueError(f'node: {end} not reachable from node: {start}')
