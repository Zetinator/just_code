"""implementation of the dijkstra algorithm
https://www.youtube.com/watch?v=GazC3A4OQTE
https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
"""
from data_structures import wgraph
from data_structures import min_heap

def retrieve_path(parents: dict, end):
    """returns the path from start to the given end
    """
    path = [end]
    current_node = end
    while parents[current_node] != None:
        path.append(parents[current_node])
        current_node = parents[current_node]
    path.reverse()
    return path

# stop once end from start is found
def dijkstra(graph: wgraph.WGraph, start, end) -> list:
    """returns when the first path is found from the start node to the end node
    creates the topological order first and the the path to node: end is retrived
    
    not optimal... still missing the fibonacci heap
    this one works making an aditional pop when the node is already in the 'path'
    """
    # set-up
    parents = dict()
    heap = min_heap.Heap([(0, start, None)])
    while heap:
        current_distance, current_node, parent = heap.pop()
        # no revisiting...
        if current_node in parents: continue
        parents[current_node] = parent
        # match
        if current_node == end: return retrieve_path(parents, end)
        for neighbor in graph.neighbors(current_node):
            # relax a little, I'm glad I inspire you but Stan, why are you so mad?
            delta = graph.weight(current_node, neighbor) + current_distance
            heap.push((delta, neighbor, current_node))
    raise ValueError(f'node: {end} not reachable from node: {start}')
