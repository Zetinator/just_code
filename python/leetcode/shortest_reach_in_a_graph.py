"""https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=graphs

In this challenge, there is a connected undirected graph where each of the nodes is a color. Given a color, find the shortest path connecting any two nodes of that color. Each edge has a weight of 1. If there is not a pair or if the color is not found, print -1
"""

class Graph():
    """simple bidirectional graph from adjacent list
    """
    def __init__(self, n, edges):
        self.nodes = set(range(1,n+1))
        self.edges = dict()
        self.build_edges(edges)

    def build_edges(self, edges):
        for edge in edges:
            c_1, c_2 = edge
            # will be bidirectional...
            self.edges.setdefault(c_1, []).append(c_2)
            self.edges.setdefault(c_2, []).append(c_1)

    def get_neighboors(self, node):
        return self.edges.get(node, [])

    def __repr__(self):
        return repr(self.edges)


def find_all_distances(graph, start):
    """standard single source shortest path
    """
    # special case: no nodes with the give color
    if not start in graph.nodes: return
    # standard bfs...
    frontier = [start]
    parents = {start:None}
    levels = {start: 0}
    level = 1
    while frontier:
        _next = []
        for current_node in frontier:
            for neighboor in graph.get_neighboors(current_node):
                if neighboor not in parents:
                    parents[neighboor] = current_node
                    levels[neighboor] = level
                    _next.append(neighboor)
        frontier = _next
        level += 1
    # print distances...
    distances = []
    for node in range(1, len(graph.nodes)+1):
        if node == start: continue
        d = levels.get(node, -1)
        distances.append(d*6 if d != -1 else -1)
    return distances


# test
graph_nodes = 4
edges = [[1, 2],
        [1, 3]]
start = 1
graph = Graph(graph_nodes, edges)

graph_nodes = 7
edges = [[1, 2],
        [1, 3],
        [3, 4],
        [2, 5]]
start = 2
graph = Graph(graph_nodes, edges)

# t = int(input())
# for i in range(t):
    # graph_nodes, m = [int(value) for value in input().split()]
    # edges = []
    # for i in range(m):
        # x,y = [int(x) for x in input().split()]
        # edges.append((x,y))
    # start = int(input())
    # graph = Graph(graph_nodes, edges)
    # distances = find_all_distances(graph, start)
    # for i,d in enumerate(distances):
        # if i != len(distances)-1: print(d, end=' ')
        # else: print(d, end='\n')

print(f'{find_all_distances(graph, start)}')

