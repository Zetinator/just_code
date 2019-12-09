"""implementation of the depth first search algorithm
https://en.wikipedia.org/wiki/Graph_traversal#Depth-first_search
"""
from data_structures import graph

# global variables:
visited = set()
parents = {}

def retrieve_path(parents: dict, end):
    path = [end]
    current_node = end
    while parents[current_node] != None:
        path.append(parents[current_node])
        current_node = parents[current_node]
    path.reverse()
    return path

def dfs(graph: graph.Graph, start, end) -> list:
    """returns the first path found from the start node to the end node
    """
    # set-up
    visited.clear()
    parents.clear()
    parents[start] = None
    def r(graph, current_node, end):
        visited.add(current_node)
        # get nodes to visit
        neighbors = graph.neighbors(current_node)
        for node in neighbors:
            # no-revisiting
            if node in visited: continue
            print(f'visiting {current_node} --> {node}')
            parents[node] = current_node
            if node == end: return print(retrieve_path(parents, end))
            r(graph, node, end)
        return
    return r(graph, start, end)

# test
g = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }
g = graph.Graph(g)