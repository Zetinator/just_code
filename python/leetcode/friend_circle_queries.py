"""https://www.hackerrank.com/challenges/friend-circle-queries/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=miscellaneous

The population of HackerWorld is . Initially, none of the people are friends with each other. In order to start a friendship, two persons  and  have to shake hands, where . The friendship relation is transitive, that is if  and  shake hands with each other,  and friends of  become friends with  and friends of .
"""

from collections import Counter
class DJS():
    def __init__(self):
        self.parents = {}
        self.counter = Counter()
        self.max = -float('inf')

    def __repr__(self):
        return repr(self.parents)

    def find(self, node):
        # compression optimization
        if self.parents.get(node, node) != node:
            self.parents[node] = self.find(self.parents[node])
        return self.parents.get(node, node)

    def union(self, n1, n2):
        parent_1, parent_2 = self.find(n1), self.find(n2)
        if parent_1 == parent_2: return
        self.parents[parent_2] = parent_1
        self.counter[parent_1] += 1 + self.counter[parent_2]
        self.max = max(self.max, self.counter[parent_1])

def maxCircle(queries):
    """that smelly smell... like disjoint sets
    almost there... almost
    """
    djs = DJS()
    res = []
    for query in queries:
        friend_1, friend_2 = query
        djs.union(friend_1, friend_2)
        res.append(djs.max+1)
    return res

test = """1 2
3 4
1 3
5 7
5 6
7 4"""

test = """13 54
4 70
56 48
86 61
85 31
61 18
53 52
78 71
95 72
4 22
46 81
88 65
54 9
72 46
35 98
12 100
3 68
21 58
15 59
70 51
89 31
69 93
82 98
15 28
21 19
49 66
99 89
83 4
97 6
49 84
55 13
35 58
80 7
15 94
17 85
44 6
67 64
50 100
62 65
28 82
83 28
100 33
68 34
36 17
39 85
52 46
97 86
3 28
44 69
21 61
5 16
18 71
80 67
71 93
83 50
26 17
29 77
49 97
10 85
13 1
21 64
46 69
1 48
96 44
16 68
56 73
83 73
43 14
92 65
6 74
14 84
91 43
60 39
91 70
75 55
70 47
70 15
15 70
14 62
65 81
29 73
53 12
45 96
77 36
60 35
62 26
18 52
20 77
42 62
98 69
16 19
15 85
85 30
6 98
43 22
79 72
94 31
35 91
78 11
78 90"""
_t = []
for line in test.split('\n'):
    tmp = []
    for e in line.split():
        tmp.append(int(e))
    _t.append(tmp)
test = _t
print(f'testing with: {test}')
print(f'ans: {maxCircle(test)}')
ans = maxCircle(test)
