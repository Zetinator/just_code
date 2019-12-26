"""https://www.hackerrank.com/challenges/find-the-nearest-clone/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=graphs

In this challenge, there is a connected undirected graph where each of the nodes is a color. Given a color, find the shortest path connecting any two nodes of that color. Each edge has a weight of 1. If there is not a pair or if the color is not found, print -1
"""

class Graph():
    """simple bidirectional graph from adjacent list
    """
    def __init__(self, n, ids, edges):
        self.nodes = dict(zip(range(1,n+1), ids))
        self.edges = dict()
        self.colors = dict()
        for i, color in enumerate(ids,1):
            self.colors.setdefault(color, []).append(i)
        self.build_edges(edges)

    def build_edges(self, edges):
        for edge in edges:
            c_1, c_2 = edge
            # will be bidirectional...
            self.edges.setdefault(c_1, []).append(c_2)
            self.edges.setdefault(c_2, []).append(c_1)

    def get_nodes(self, color):
        return self.colors.get(color, [])

    def get_color(self, node):
        return self.nodes.get(node, None)

    def get_neighboors(self, node):
        return self.edges.get(node, [])

    def __repr__(self):
        return repr(self.edges)


def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    """standard single source shortest path
    """
    # build undirected graph
    graph = Graph(graph_nodes, ids, zip(graph_from, graph_to))
    # special case: no nodes with the give color
    if not graph.get_color(val): return -1
    # standard bfs...
    def bfs(start):
        frontier = [start]
        parents = {start:None}
        level = 1
        while frontier:
            _next = []
            for current_node in frontier:
                for neighboor in graph.get_neighboors(current_node):
                    if neighboor not in parents:
                        if graph.get_color(neighboor) == val: return level
                        parents[neighboor] = current_node
                        _next.append(neighboor)
            frontier = _next
            level += 1
        return float('inf')
    # get all the nodes of the given color
    searchable_nodes = graph.get_nodes(val)
    minimum = float('inf')
    for start in searchable_nodes:
        d = bfs(start)
        if minimum > d: minimum = d
    return minimum if minimum != float('inf') else -1

# test
graph_nodes = 4
edges = [[1, 2],
        [1, 3],
        [4, 2]]
graph_from = [f for f, t in edges]
graph_to = [t for f, t in edges]
ids = [1, 2, 1, 1]
val = 1

graph = Graph(graph_nodes, ids, edges)
print(f'{findShortest(graph_nodes, graph_from, graph_to, ids, val)}')
