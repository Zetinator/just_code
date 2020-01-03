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
        def __init__(self, data=None, index=None):
            self.data = data
            self.left = None
            self.right = None
            # just for visualization purposes...
            self.index = index

    def __init__(self, v):
        self.v = v
        self.build()

    def __len__(self):
        return len(self.v)

    def build(self):
        """build the segment tree from the given array v
        """
        if not self.v: return
        L, R = 0, len(self.v)-1
        def r_build(L, R):
            # base case: just one element in the interval
            if L == R: return self.Node(self.v[L], (L,R))
            # divide
            m = (L+R)//2
            node = self.Node()
            node.left, node.right = r_build(L, m), r_build(m+1, R)
            # conquer
            get_val = lambda x: x.data if x else -float('inf')  # None -> -inf
            node.data = max(get_val(node.left), get_val(node.right))
            node.index=((L,R))
            return node
        self.root = r_build(L, R)
            
    def query(self, i, j):
        """return max in the given range (i,j) inclusive, O(log(N))
        """
        if not self.root: return
        # special case: invalid range as input
        if not 0 <= i <= j < len(self.v): raise ValueError(f'invalid range: {(i,j)}')
        L, R = 0, len(self.v)-1
        # modified binary search...
        def r(node, L, R, i, j):
            if i > j: return -float('inf')
            if i <= L <= R <= j: return node.data
            m = (L+R)//2
            return max(r(node.left, L, m, i, min(m, j)),
                        r(node.right, m+1, R, max(i, m+1), j))
        return r(self.root, L, R, i, j)

    def __repr__(self):
        res = []
        def r(node, level=0):
            if not node: return
            r(node.left, level+1)
            res.append('\t'*level + f'-->({node.data})[{node.index}]')
            r(node.right, level+1)
        r(self.root)
        return '\n'.join(res)
