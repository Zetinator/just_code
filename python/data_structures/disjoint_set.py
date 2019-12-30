"""custom implementation of a union-find disjoint set with the purpose of practice
the ADT contains the following methods:
    - find
    - union
    - same
"""
class DJS():
    """hashmap implementation
    """
    def __init__(self):
        self.parents = dict()

    def __repr__(self):
        return repr(self.parents)

    def __len__(self):
        return len(self.parents)

    def find(self, node):
        """traverse the tree until the root
        """
        # path compression
        if self.parents.get(node, node) != node:
            self.parents[node] = self.find(self.parents[node])
        return self.parents.get(node, node)

    def same(self, node_1, node_2):
        """traverse the tree until the root
        if the roots are the same, they are in the same set
        """
        root_1, root_2 = self.find(node_1), self.find(node_2)
        return root_1 == root_2

    def union(self, node_1, node_2):
        """we make the union of two disjoint sets
        the path compression makes it optimal, without the rank optimization
        """
        root_1, root_2 = self.find(node_1), self.find(node_2)
        if root_1 == root_2: return
        # add the short to the big
        if node_1 == root_1: self.parents[root_1] = root_2
        else: self.parents[root_2] = root_1
