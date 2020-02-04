"""custom implementation of a van emde boas tree with the purpose of practice

https://www.youtube.com/watch?v=hmReJCupbNU&t=1838s
https://en.wikipedia.org/wiki/Van_Emde_Boas_tree

the ADT contains the following methods:
    - insert: insert a new node in the tree
    - search: return the node with the given value
    - delete: delete the given value from the tree
    - successor: return the next in order successor
"""
from math import ceil
class VEB:
    """this data structurethis data structure allows log(log(U)) computations on integer keys
    """
    class Node():
        """Node basic chainable storage unit
        each node has the same basic structure: u, min, max, summary, clusters
        """
        def __init__(self, u):
            # initial set-up: u, min, max
            self.u = u
            self.min = self.max = None
            # set clusters and summary
            n = int(self.u**(1/2))
            # if universe is not greater than 2 is enough to store min and max 
            self.clusters = [None for _ in range(n)] if self.u > 2 else []
            self.summary = None
        def __repr__(self):
            return f'{(self.min, self.max)}u{self.u}'

    def __init__(self, keys=[], u=None):
        # find the size of universe (next power of 2 containing all the keys)
        self.u, maximum = 2, u or max(keys)
        while self.u < maximum: self.u = self.u<<1
        # build tree from root
        self.root = self.Node(self.u)
        self.build()
        # insert elements in the tree
        for key in keys:
            self.insert(key)

    def build(self):
        """build tree top-down
        """
        # build recursively...
        def r(node):
            if not node: return
            if node.clusters:
                n = len(node.clusters)
                for i in range(n):
                    node.clusters[i] = self.Node(n)
                    r(node.clusters[i])
                node.summary = self.Node(n)
                r(node.summary)
        r(self.root)

    def __repr__(self):
        """print first the main tree and the clusters recursevly
        then print the summary tree recursively
        """
        main, summary = [], []
        def r(tmp, node, level=0):
            if not node: return
            tmp.append('\t'*level + f'-->{node}')
            for cluster in node.clusters:
                r(tmp, cluster, level+1)
        # recurse on both the main and the summary tree
        r(main, self.root); r(summary, self.root.summary)
        main, summary = '\n'.join(main), '\n'.join(summary)
        return f'main:\n{main}\nsummary:\n{summary}'

    def __len__(self):
        return self.u

    def min(self):
        """returns min in O(1)
        """
        return self.root.min

    def max(self):
        """returns max in O(1)
        """
        return self.root.max

    def search(self, key):
        """find key in the tree in O(lg lg u)
        """
        # aux indexing functions
        high = lambda x: int(x//(self.u**(1/2)))
        low = lambda x: x % int(ceil(self.u**(1/2)))
        # let's recurse, shall we?...
        def r(node, x):
            print(f'node: {node}')
            if node.min == x or node.max == x: return True
            # keep looking...
            if node.clusters: return r(node.clusters[high(x)], low(x))
        return r(self.root, key)

    def insert(self, key):
        """insert a new key in the tree
        """
        if not (0 <= key < self.u): raise ValueError(f'{key} out of universe')
        # aux indexing functions
        high = lambda x: int(x//(self.u**(1/2)))
        low = lambda x: x % int(ceil(self.u**(1/2)))
        # insert recursively
        def r(node, x):
            # pseudo lazy propagation, makes the insertion log(log(U))
            if not node.min: node.min = node.max = x; return
            if node.min and x < node.min: x, node.min = node.min, x
            if node.max and x > node.max: node.max = x
            # update summary if the cluster was empty
            i, j = high(x), low(x)
            if node.clusters and not node.clusters[i].min: r(node.summary, i)
            if node.clusters: r(node.clusters[i], j)
        return r(self.root, key)

    def successor(self, key):
        """returns the successor of the given key in the tree
        """
        if self.root.min == None: return
        # aux indexing functions
        high = lambda x: int(x//(self.u**(1/2)))
        low = lambda x: x % int(ceil(self.u**(1/2)))
        def r(node, x):
            print(f'current_node: {node}, key: {x}')
            # easy case...
            if x < node.min: return node.min
            # no successor availible...
            if x > node.max: return node.u
            i, j = high(x), low(x)
            # print(f'j: {j}, node.clusters[i].max: {node.clusters[i].max}')
            if node.clusters and node.clusters[i].max and j < node.clusters[i].max:
                # look in the corresponding cluster
                print(f'search in the cluster: {node.clusters[i]}')
                j = r(node.clusters[i], j)
            else:
                # take a look in the summary first
                print(f'take a look in the summary: {node.summary}')
                i = r(node.summary, i) if node.summary else i
                print(f'take a look in the cluster {i}: {node.clusters}')
                j = node.clusters[i].min if node.clusters else j
            print(f'returning: i: {i}, j: {j}')
            return i*int(node.u**(1/2)) + j
        return r(self.root, key)

    def delete(self, x):
        """
        Deletes an element x in the universe of size u
        """
        if self.min == self.max:
            self.min = None
            self.max = None
        elif self.u == 2:
            if x == 0:
                self.min = 1
            else:
                self.min = 0

            self.max = self.min
        else:
            if x == self.min:
                first_cluster = self.summary.getMin()
                x = self.index(first_cluster, self.clusters[first_cluster].getMin())
                self.min = x

            self.clusters[self.high(x)].delete(self.low(x))

            if self.clusters[self.high(x)].getMin() is None:
                self.summary.delete(self.high(x))

                if x == self.max:
                    summary_max = self.summary.getMax()
                    if summary_max is None:
                        self.max = self.min
                    else:
                        self.max = self.index(summary_max, self.clusters[summary_max].getMax())
            elif x == self.max:
                self.max = self.index(self.high(x), self.clusters[self.high(x)].getMax())

# test = [32, 3, 36, 26, 7, 46, 49, 52, 58]
# test = [31, 3, 26, 7, 10]
test = [15, 3, 10, 12, 5]
test = [1,3,5,7]
test = [1,2,3,5,8,10]
test = [2,3,4,5,7,14,15]
v = VEB(u=16, keys=test)
