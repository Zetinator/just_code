"""https://www.hackerrank.com/challenges/components-in-graph/problem
the same problem as the circles of friends... but they request the minimum as well...
"""
#!/bin/python3

import os
import sys

#
# Complete the componentsInGraph function below.
import sys
sys.setrecursionlimit(100000)
from collections import Counter
class DJS():
    """https://en.wikipedia.org/wiki/Disjoint-set_data_structure
    """
    def __init__(self):
        self.parents = {}
    def find(self, node):
        """with path compression
        """
        if self.parents.get(node, node) != node:
            self.parents[node] = self.find(self.parents[node])
        return self.parents.get(node, node)
    def union(self, n1, n2):
        parent_1, parent_2 = self.find(n1), self.find(n2)
        # already in the same set... nothing to do here
        if parent_1 == parent_2: return
        self.parents[parent_1] = parent_2

def componentsInGraph(gb):
    """that smelly smell like... disjoint sets
    """
    djs = DJS()
    counter = Counter()
    # group the connected components
    for q in gb:
        n1, n2 = q
        djs.union(n1, n2)
    # count the members per group...
    for n in djs.parents:
        counter[djs.find(n)] += 1
    ans = counter.most_common()
    return [ans[-1][1]+1,ans[0][1]+1]

if __name__ == '__main__':

    gb = []
    with open('./test_data.txt', 'r') as f:
        for line in f:
            gb.append([int(n) for n in line.split()])

    result = componentsInGraph(gb)

    print(result)

