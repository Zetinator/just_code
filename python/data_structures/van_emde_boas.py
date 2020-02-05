"""custom implementation of a van emde boas tree with the purpose of practice

This one uses hash tables to achive O(n*log(log(U))) efficiency, instead of the original O(U)
where: n is the number of elements in the tree, and U is the size of the 'universe'

https://www.youtube.com/watch?v=hmReJCupbNU&t=1838s
https://en.wikipedia.org/wiki/Van_Emde_Boas_tree

the ADT contains the following methods:
    - insert: insert a new node in the tree in O(lg lg u)
    - search: return the node with the given value in O(lg lg u)
    - min: return the min element in O(1)
    - max: returns the max element in O(1)
    - delete: delete the given value from the tree in O(lg lg U)
    - successor: return the next in order successor in O(lg lg U)

usage example:
     v = VEB([33, 66, 1, 65, 5, 7, 41])
     v = VEB(u=16, keys=[1,3,5,11])
"""
class VEB:
    class Node():
        """Node basic chainable storage unit
        each node has the same basic structure: u, min, max, summary, clusters
        """
        def __init__(self, u):
            # initial set-up: u, min, max
            self.u = 2
            # find the size of universe (next power of 2 containing all the keys)
            while self.u < u: self.u = self.u<<1
            self.min = self.max = None
            # set clusters and summary
            self.clusters = {}
            self.summary = None
        def __repr__(self):
            return f'{(self.min, self.max)}u{self.u}'

    def __init__(self, keys=[], u=None):
        # find the size of universe (next power of 2 containing all the keys)
        self.u, maximum = 2, u or max(keys)
        while self.u < maximum: self.u = self.u<<1
        # build tree from root
        self.root = self.Node(self.u)
        # insert elements in the tree
        for key in keys:
            self.insert(key)

    def __repr__(self):
        """print first the main and summary trees recursevly
        """
        main, summary = [], []
        def r(tmp, node, level=0):
            if not node: return
            tmp.append('\t'*level + f'-->{node}')
            for k, cluster in node.clusters.items():
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
        # search recursively
        def r(node, x):
            if node.min == x or node.max == x: return True
            # get cluster -> i (high) and offset -> j (low)
            i = x//int(node.u**(1/2))
            j = x % int(node.u**(1/2))
            # don't give up... keep looking!
            if i in node.clusters: return r(node.clusters[i], j)
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
            i = x//int(node.u**(1/2))
            j = x % int(node.u**(1/2))
            u = int(node.u**(1/2))
            # update summary if the corresponding cluster was empty
            if node.u > 2 and i not in node.clusters:
                if not node.summary: node.summary = self.Node(u)
                r(node.summary, i)
            # update the corresponding cluster
            if node.u > 2: r(node.clusters.setdefault(i, self.Node(u)), j)
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
            i = x//int(node.u**(1/2))
            j = x % int(node.u**(1/2))
            # professor Erik Demaine was missing this next line...
            if not node.u > 2 and x < node.max: return node.max
            if node.u > 2 and i in node.clusters and j < node.clusters[i].max:
                # if key < max in the cluster for sure the successor can be found here
                j = r(node.clusters[i], j)
            else:
                # take a look in the summary first
                i = r(node.summary, i)
                j = node.clusters[i].min
            return i*int(node.u**(1/2)) + j
        return r(self.root, key)

    def delete(self, key):
        """deletes an element x in the tree in O(log log U)
        """
        if self.root.min is None: return
        # delete recursively
        def r(node, x):
            # base case: we reached a node with a single element
            # return a signal to the parent to erase this empty child
            if node.min == node.max: return True
            # special case: erasing min
            if x == node.min:
                # we dont want to recurse into a node with no summary...
                if not node.u > 2: node.min = node.max; return
                tmp = node.summary.min
                # new min discovered, update
                x = node.min = tmp*int(node.u**(1/2)) + node.clusters[tmp].min
            # get cluster -> i (high) and offset -> j (low)
            i = x//int(node.u**(1/2))
            j = x % int(node.u**(1/2))
            # simetrical with respect to insert, we delete first
            if node.u > 2 and i in node.clusters:
                if r(node.clusters[i], j): del(node.clusters[i])
            # then if is the cluster is empty, update the summary
            if node.u > 2 and i not in node.clusters: r(node.summary, i)
            # special case: erasing max, very similar to the min case
            if x == node.max:
                if not node.clusters:
                    node.max = node.min
                    node.summary = None
                    return
                tmp = node.summary.max
                if tmp in node.clusters:
                    node.max = tmp*int(node.u**(1/2)) + node.clusters[tmp].max
        if r(self.root, key): self.root = self.Node(self.root.u)
