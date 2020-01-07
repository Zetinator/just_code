"""https://www.hackerrank.com/challenges/kittys-calculations-on-a-tree/problem

Kitty has a tree, , consisting of  nodes where each node is uniquely labeled from  to . Her friend Alex gave her  sets, where each set contains  distinct nodes. Kitty needs to calculate the following expression on each set:
"""

class Graph():
    def __init__(self, edges):
        self.nodes = set()
        self.edges = {}
        self.weights = {}
        self.build_edges(edges)
    def build_edges(self, edges):
        for edge in edges:
            n1, n2 = edge
            self.nodes.add(n1); self.nodes.add(n2)
            self.edges.setdefault(n1, []).append(n2)
            self.edges.setdefault(n2, []).append(n1)
    def neiboors(self, node):
        return self.edges.get(node, [])

def floyds(graph):
    d = []
    n_nodes = len(graph.nodes)+1
    d = [[float('inf')]*n_nodes for _ in range(n_nodes)]
    for i in range(n_nodes):
        d[i][i] = 0
    for edge in edges:
        u, v = edge
        d[u][v], d[v][u] = 1, 1
    for k in range(n_nodes-1):
        for u in range(n_nodes):
            for v in range(n_nodes):
                d[u][v] = min(d[u][v], d[u][k] + d[k][v])
    return d

from itertools import combinations
def solve(edges, sets):
    graph = Graph(edges)
    d = floyds(graph)
    res = []
    for s in sets:
        if len(s) == 1:
            res.append(0); continue
        tmp = 0
        for n1, n2 in combinations(s, 2):
            tmp += n1 * n2 * d[n1][n2]
        res.append(tmp)
    return d

# read from stdin
n, q = [int(i) for i in input().split()]
edges, sets = [], []
for _ in range(n-1):
    edges.append([int(i) for i in input().split()])
for _ in range(q):
    k = input()
    sets.append([int(i) for i in input().split()])
res = solve(edges, sets)
# for line in res: print(line)

# local test
# edges = [[1, 2], [1, 3], [1, 4], [3, 5], [3, 6], [3, 7]]
# sets = [[2, 4], [5], [2, 4, 5]]
# res = solve(edges, sets)
# graph = Graph(edges)
# for line in res:
    # print(line)
