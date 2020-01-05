"""custom implementation of a segment tree with the purpose of practice
https://en.wikipedia.org/wiki/Segment_tree
the ADT contains the following methods:
    - build: build tree from the given array
    - query: max query on the given range
"""
class ST():
    class Node():
        """Node basic chainable storage unit
        """
        def __init__(self, value=None, index=None):
            self.value = value
            self.left = None
            self.right = None
            # just for visualization purposes...
            self.index = index
        def __repr__(self):
            return repr(self.value)

    def __init__(self, v):
        self.v = v
        self.build()

    def __len__(self):
        return len(self.v)

    def build(self):
        """build the segment tree from the given array v
        """
        if not self.v: return
        l, r = 0, len(self.v)-1
        def r_build(l, r):
            # base case: just one element in the interval
            if l == r: return self.Node(self.v[l], (l,r))
            # divide
            m = (l+r)//2
            node = self.Node()
            node.left, node.right = r_build(l, m), r_build(m+1, r)
            # conquer
            get_val = lambda x: x.value if x else -float('inf')  # None -> -inf
            node.value = max(get_val(node.left), get_val(node.right))
            node.index=((l,r))
            return node
        self.root = r_build(l, r)
            
    def query(self, i, j):
        """return max in the given range (i,j) inclusive, O(log(N))
        """
        if not self.root: return
        # special case: invalid range as input
        if not 0 <= i <= j < len(self.v): raise ValueError(f'invalid range: {(i,j)}')
        l, r = 0, len(self.v)-1
        # modified binary search...
        def r_query(node, l, r, i, j):
            if not node or l > r or i > r or j < l: return -float('inf')
            if i <= l <= r <= j: return node.value
            m = (l+r)//2
            return max(r_query(node.left, l, m, i, j),
                        r_query(node.right, m+1, r, i, j))
        return r_query(self.root, l, r, i, j)

    def __repr__(self):
        res = []
        def r(node, level=0):
            if not node: return
            r(node.left, level+1)
            res.append('\t'*level + f'-->({node.value})[{node.index}]')
            r(node.right, level+1)
        r(self.root)
        return '\n'.join(res)
