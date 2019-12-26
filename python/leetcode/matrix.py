"""https://www.hackerrank.com/challenges/matrix/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=graphs

The kingdom of Zion has cities connected by bidirectional roads. There is a unique path between any pair of cities. Morpheus has found out that the machines are planning to destroy the whole kingdom. If two machines can join forces, they will attack. Neo has to destroy roads connecting cities with machines in order to stop them from joining forces. There must not be any path connecting two machines.

Each of the roads takes an amount of time to destroy, and only one can be worked on at a time. Given a list of edges and times, determine the minimum time to stop the attack.

For example, there are  cities called . Three of them have machines and are colored red. The time to destroy is shown next to each road. If we cut the two green roads, there are no paths between any two machines. The time required is .
"""

class Graph():
    """simple bidirectional graph from adjacent list
    with weights...
    """
    def __init__(self, edges, machines):
        self.nodes = set()
        self.machines = set(machines)
        self.edges = dict()
        self.weights = dict()
        self.total_w = 0
        self.build_graph(edges)

    def build_graph(self, edges):
        for edge in edges:
            c_1, c_2, weight = edge
            self.nodes.add(c_1); self.nodes.add(c_2)
            # will be bidirectional...
            self.edges.setdefault(c_1, []).append(c_2)
            self.edges.setdefault(c_2, []).append(c_1)
            # weights
            self.total_w += weight
            self.weights[(c_1, c_2)] = weight

    def has_machine(self, node):
        return node in self.machines

    def weight(self, x, y):
        return self.weights.get((x,y), None) or self.weights.get((y,x), None)

    def neighbors(self, node):
        return self.edges.get(node, [])

    def __repr__(self):
        return repr(self.edges)

class Heap():
    """max heap
    """
    def __init__(self, x=[]):
        self.v = []
        for e in x:
            self.push(e)

    def __repr__(self):
        return repr(self.v)
    
    def __len__(self):
        return len(self.v)

    def push(self, x):
        # set-up...
        v, i = self.v, len(self.v)
        v.append(x)
        # call parent
        parent = lambda: max((i-1)//2, 0)
        while v[i] > v[parent()]:
            v[parent()], v[i] = v[i], v[parent()]
            i = parent()

    def peek(self):
        if not self.v: return
        return self.v[0]

    def pop(self):
        if not self.v: return
        # set-up...
        v, i = self.v, 0
        # initial swap...
        v[0], v[-1] = v[-1], v[0]
        res = v.pop()
        # call child
        left = lambda: i*2+1 if i*2+1 < len(v) else False
        right = lambda: i*2+2 if i*2+2 < len(v) else False
        while (left() and v[left()] > v[i] or
                right() and v[right()] > v[i]):
            min_child = left()
            if right() and v[right()] > v[left()]:
                min_child = right()
            v[min_child], v[i] = v[i], v[min_child]
            i = min_child
        return res

def minTime(roads, machines):
    """trying modified prim's algorithm
    instead of the min spanning tree is the max spanning tree
    and we allow just one city with a machine in the max spanning tree

    the algorithm is not correct...
    """
    # set-up
    graph = Graph(roads, machines)
    minTime.mst = 0
    nodes = set()
    def prim(start):
        # get first frontier
        q = Heap([(graph.weight(start, node), node, start) for node in graph.neighbors(start)])
        machine_flag = graph.has_machine(start)
        nodes.add(start)
        while q:
            weight, current_node, parent = q.pop()
            # no revisiting
            if current_node in nodes: continue
            nodes.add(current_node)
            # no double machines
            if machine_flag and graph.has_machine(current_node): continue
            # only one machine allowed
            if not machine_flag and graph.has_machine(current_node): machine_flag = True
            minTime.mst += graph.weight(parent, current_node)
            print(f'start: {start}, visiting: {current_node}, from: {parent}, flag: {machine_flag}')
            for neighbor in graph.neighbors(current_node):
                q.push((graph.weight(current_node,neighbor), neighbor, current_node))
    # do not start with a machine...
    to_try = list(graph.nodes-set(machines))
    for start in to_try:
        prim(start)
    res = graph.total_w - minTime.mst
    print(f'max_span: {minTime.mst}, total: {graph.total_w}, remaining: {res}')
    return res

def minTime(roads, machines):
    """kruskal algorithm
    with union find disjoint
    """
    parents = {}
    # dp[i] denotes whether or not component with root i had already had a machine
    dp = dict().fromkeys(range(len(roads)+1), 0)
    for machine in machines:
        dp[machine] = 1
    def find(node):
        if parents.get(node, node) == node:
            return node
        return find(parents[node])
    def union(c1,c2):
        x,y = find(c1), find(c2)
        # if the roots are not a machine
        if not dp[x] or not dp[y]:
            if c1 != x : x,y = y,x
            parents[x] = y
            dp[x] |= dp[y]
            dp[y] |= dp[x]
            return True
    return sum(w for c1,c2,w in sorted(roads, key=lambda x: -x[2]) if not union(c1,c2))

# test
roads = [[2, 1, 8],
        [1, 0, 5],
        [2, 4, 5],
        [1, 3, 4]]
machines = [2,4,0]

roads = [[0,1,4],
        [1,2,3],
        [1,3,7],
        [0,4,2]]
machines = [2,3,4]

machines = """1
95
90
11
48
49
23
6
0
76
3
83
85
31
44
54
87
38
16
61
22
21
29""".split('\n')
machines = [int(n) for n in machines]
roads ="""9 78 35
9 54 45
78 69 27
9 55 9
9 1 78
1 92 7
55 42 57
1 84 4
1 5 38
92 8 75
55 30 99
69 7 9
1 81 45
8 31 4
42 23 100
78 95 3
54 14 14
84 53 80
92 32 8
42 86 40
1 64 93
78 60 65
64 76 24
42 89 86
7 28 48
69 62 26
1 40 23
78 38 29
8 44 39
78 3 37
54 26 17
62 50 24
76 66 37
30 51 75
86 43 91
5 77 32
64 91 11
14 10 36
26 20 19
9 52 50
77 94 32
44 67 63
64 15 61
92 0 73
10 37 23
89 2 37
92 18 51
26 47 25
30 87 15
47 36 35
92 72 16
28 75 93
78 73 66
20 19 64
73 57 1
91 6 50
54 33 41
78 11 38
37 71 55
5 63 52
10 46 22
94 82 19
95 83 51
57 90 10
63 58 94
43 45 23
72 68 62
82 85 88
58 4 94
82 41 62
3 22 68
54 70 78
31 74 27
36 29 61
33 24 76
40 35 61
83 79 51
8 59 20
45 34 26
38 12 18
70 99 25
40 80 81
31 97 58
69 21 16
83 13 22
80 48 49
97 65 44
74 17 1
68 16 92
50 98 54
94 27 76
81 61 67
85 49 96
81 93 31
22 25 67
57 96 93
82 88 92
86 56 80
25 39 44""".split('\n')
roads_pp= []
for line in roads: 
    l = []
    for n in line.split():
        l.append(int(n))
    roads_pp.append(l)

# print(f'roads: {roads}')
print(f'machines: {machines}')
graph = Graph(roads_pp, machines)
print(f'ans: {minTime(roads_pp, machines)}')
