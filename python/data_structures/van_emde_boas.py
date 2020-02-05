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
        """find key in the tree in O(log log u)
        """
        # aux indexing functions
        high = lambda x: int(x//(self.u**(1/2)))
        low = lambda x: x % int(ceil(self.u**(1/2)))
        # search recursively
        def r(node, x):
            if node.min == x or node.max == x: return True
            # don't give up... keep looking!
            if node.clusters: return r(node.clusters[high(x)], low(x))
        return r(self.root, key)

    def insert(self, key):
        """insert a new key in O(log log u)
        """
        if not (0 <= key < self.u): raise ValueError(f'{key} out of universe')
        # insert recursively
        def r(node, x):
            # pseudo lazy propagation, makes the insertion log(log(U))
            if node.min is None: node.min = node.max = x; return
            if x < node.min: x, node.min = node.min, x
            if x > node.max: node.max = x
            # get cluster -> i (high) and offset -> j (low)
            i = int(x//(node.u**(1/2)))
            j = x % int(ceil(node.u**(1/2)))
            # update summary if the corresponding cluster was empty
            if node.clusters and node.clusters[i].min is None: r(node.summary, i)
            # update the corresponding cluster
            if node.clusters: r(node.clusters[i], j)
        return r(self.root, key)

    def successor(self, key):
        """returns the successor of the given key in the tree
        """
        if self.root.min is None: return
        def r(node, x):
            # trivial case
            if x < node.min: return node.min
            # no successor availible...
            if x >= node.max: return node.u
            # get cluster -> i (high) and offset -> j (low)
            i = int(x//(node.u**(1/2)))
            j = x % int(ceil(node.u**(1/2)))
            # professor Erik Demaine was missing this next line...
            if not node.clusters and x < node.max: return node.max
            if node.clusters and node.clusters[i].max is not None and j < node.clusters[i].max:
                # if key < max in the cluster for sure the successor can be found here
                j = r(node.clusters[i], j)
            else:
                # take a look in the summary first
                i = r(node.summary, i) if node.summary else i
                j = node.clusters[i].min if node.clusters else j
            return i*int(node.u**(1/2)) + j
        return r(self.root, key)

    def delete(self, key):
        """deletes an element x in the tree in O(log log U)
        """
        if self.root.min is None: return
        # delete recursively
        def r(node, x, level=0):
            # get cluster -> i (high) and offset -> j (low)
            i = int(x//(node.u**(1/2)))
            j = x % int(ceil(node.u**(1/2)))
            print('  '*level + f'current_node: {node}')
            print('  '*level + f'successor of key: {x}, in i: {i}, j: {j}')
            # special case: erasing min
            if x == node.min:
                print('  '*level + f'x: {x} == node.min: {node.min}')
                if not node.summary or node.summary.min is None:
                    node.min = node.max = None; return
                print('  '*level + f'{node.min} -> {i*int(node.u**(1/2)) + node.clusters[i].min}')
                x = node.min = i*int(node.u**(1/2)) + node.clusters[i].min
                print('  '*level + f'changed')
            # simetrical with respect to insert
            if node.clusters: r(node.clusters[i], j, level+1)
            # is the cluster is empty, update the summary
            if node.clusters and node.clusters[i].min is None: r(node.summary, i, level+1)
            # special case: erasing max
            if x == node.max:
                print('  '*level + f'x: {x} == node.max: {node.max}')
                if not node.summary or node.summary.max is None:
                    node.max = node.min; return
                print('  '*level + f'summary: {node.summary}')
                i = node.summary.max
                node.max = i*int(node.u**(1/2)) + node.clusters[i].max
        return r(self.root, key)

# test = [32, 3, 36, 26, 7, 46, 49, 52, 58]
# test = [31, 3, 26, 7, 10]
test = [15, 3, 10, 12, 5]
test = [1,3,5,7]
test = [1,2,3,5,8,10]
test = [2,3,4,5,7,14,15]
v = VEB(u=16, keys=test)