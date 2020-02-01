"""implementation of the dinic's algorithm
https://visualgo.net/en/maxflow
https://en.wikipedia.org/wiki/Dinic%27s_algorithm
"""
from data_structures import network_graph


def dinic(graph: network_graph.NGraph, source, sink) -> int:
    """computes the maximum flow value of the network
    """
    # set-up
    parents = {source:None}
    residual_network = {k:graph.capacity(*k) for k in graph.edges}
    max_flow = 0
    print(residual_network)
    frontier = [source]
    level = 1
    # retrieve bottle neck function
    def blocking_flow(node, minimum=float('inf')):
        """returns the path from start to the given end
        """
        print(f'current node: {node}, current_min: {minimum}')
        if not node: return minimum
        minimum = min(minimum, residual_network.get((parents[node], node), float('inf')))
        # recursively find minimum
        minimum = blocking_flow(parents[node], minimum)
        # update residual graph
        residual_network[parents[node], node] -= minimum
        return minimum
    # standard bfs
    while frontier:
        _next = []
        for current_node in frontier:
            for node in graph.neighbors(current_node):
                if node == sink:
                    print(f'sink reached retrieving path at level: {level}')
                    parents[node] = current_node
                    # increase max-flow...
                    max_flow += blocking_flow(sink)
                    print(f'current max flow is: {max_flow}')
                if node not in parents:
                    _next.append(node)
                    parents[node] = current_node
                    # print(f'visiting node: {node} from: {current_node}, level: {level}')
        level += 1
        frontier = _next
