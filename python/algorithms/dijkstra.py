"""implementation of the dijkstra algorithm
https://www.youtube.com/watch?v=GazC3A4OQTE
https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
"""
from data_structures import wgraph

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
    
    unfortunately not optimal... the priority queue is been replace with a normal dictionary
    """
    # set-up
    get_min = lambda q: min([(k,v) for k,v in q.items()], key=lambda x: x[1])[0]
    parents = {start: None}
    q = dict().fromkeys(graph.nodes, float('inf'))
    q[start] = 0
    while q:
        current_node = get_min(q)
        # print(f'STATUS: q:{q}, {current_node}') 
        # match
        if current_node == end: return retrieve_path(parents, end)
        for neighbor in graph.neighbors(current_node):
            # relax a little, I'm glad I inspire you but Stan, why are you so mad?
            delta = graph.weight(current_node, neighbor) + q[current_node]
            if q[neighbor] > delta:
                q[neighbor] = delta
                parents[neighbor] = current_node
        del(q[current_node])
    raise ValueError(f'node: {end} not reachable from node: {start}')

graph = {0: [(1, 1),(2, 7)],
          1 : [(3, 9), (5, 15)],
          2 : [(4, 4)],
          3 : [(4, 10), (5, 5)],
          4 : [(5, 3)],
          5 : []
        }
graph = wgraph.WGraph(graph)
