"""custom implementation of a fenwick tree (binary indexed tree) with the purpose of practice
the ADT contains the following methods:
    - update
    - sum_until
    - sum_range
    - build
"""

class FenwickTree():
    def __init__(self, x=[]):
        self.v = [0]*(len(x))
        # 1 based arrays the lenght of the tree increases by 1
        self.tree = [0]*(len(x)+1)
        self.build(x)

    def __repr__(self):
        return repr(self.tree)

    def __len__(self):
        return len(self.v)

    def build(self, x):
        """build the fenwick tree
        """
        for i, e in enumerate(x):
            self.update(i, e)

    def update(self, i, value):
        """update the value of the given index
        """
        delta, self.v[i] = value - self.v[i], value
        # easy bit-wise computations if the indexes start at 1
        i, n = i+1, len(self.tree)
        while i < n:
            self.tree[i] += delta
            # go to parent... next powers of 2
            i += i & (-i)

    def sum_until(self, i):
        """get the sum of the range [0, i]
        """
        # limit the range of the queries to the addressable space
        i = len(self.v) if len(self.v) < i else i
        acc = 0
        while i > 0:
            acc += self.tree[i]
            # traverse all the log(n) children
            i -= i & (-i)
        return acc

    def sum_range(self, _from, _to):
        """get the sum of the range [_from, _to]
        """
        return self.sum_until(_to) - self.sum_until(_from)
