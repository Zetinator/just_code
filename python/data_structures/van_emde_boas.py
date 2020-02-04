"""custom implementation of a van emde boas tree with the purpose of practice

https://www.youtube.com/watch?v=hmReJCupbNU&t=1838s
https://en.wikipedia.org/wiki/Van_Emde_Boas_tree

the ADT contains the following methods:
    - insert: insert a new node in the tree
    - search: return the node with the given value
    - delete: delete the given value from the tree
    - successor: return the next in order successor
"""

class VEB:
    """this data structurethis data structure allows log(log(U)) computations on integer keys
    """
    def __init__(self, keys):
        # find the size of universe (next power of 2 containing all the keys)
        self.u, maximum = 2, max(keys)
        while self.u < maximum: self.u = self.u<<1
        self.root = self.Node(self.u)
        for key in keys:
            self.insert(key)

    def __len__(self):
        return self.u

    class Node():
        """Node basic chainable storage unit
        each node has the same basic structure: u, min, max, summary, clusters
        """
        def __init__(self, u):
            # set-up: u, min, max
            self.u = u
            self.min = self.max = None
            # if universe is not greater than 2 is enough to store min and max 
            if self.u <= 2: return
            # set clusters and summary
            ceil = lambda x: -int(-(x)//1)
            n = ceil(self.u**(1/2))
            self.clusters = [None for _ in range(n)]
            self.summary = None

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
        low = lambda x: x % int(self.u**(1/2))
        # let's recurse, shall we?...
        def r(node, x):
            if node.min == x or node.max == x: return True
            # keep looking...
            if node.clusters: return r(node.clusters[high(x)], low(x))
        return r(self.root, x)

    def insert(self, key):
        """insert a new key in the tree
        """
        # aux indexing functions
        high = lambda x: int(x//(self.u**(1/2)))
        low = lambda x: x % int(self.u**(1/2))
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
        if x < node.min: return node.min
        # aux indexing functions
        high = lambda x: int(x//(self.u**(1/2)))
        low = lambda x: x % int(self.u**(1/2))
        def r(node, x):
            if x < node.min: return node.min
            i, j = high(x), low(x)
            if node.clusters and j < node.clusters[i].max:
                # look in the corresponding cluster
                j = r(node.clusters[i], j)
            else:
                # not there... look in the summary
                i = r(node.summary, i)
                j = node.clusters[i].min
            return i*int(node.u**(1/2)) + j

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

test = [32, 3, 36, 26, 7, 46, 49, 52, 58]
veb = VEB(test)
