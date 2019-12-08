"""custom implementation of a segment tree with the purpose of practice
https://en.wikipedia.org/wiki/Segment_tree
the ADT contains the following methods:
    - build
    - query
    - traverse
"""
class ST():
    class Node():
        """Node basic chainable storage unit
        """
        def __init__(self, data=None, index=None):
            self.data = data
            self.index = index
            self.left = None
            self.right = None

    def __init__(self, v):
        self.v = v
        self.build()

    def build(self):
        if not self.v: return
        self.root = self.Node()
        L, R = 0, len(self.v)-1
        def r_build(current_node, L, R):
            # base case: L > R
            if L > R: return
            # base case: just one element in the interval
            if L == R:
                return self.Node(self.v[L], (L,R))
            # divide
            m = (L+R)//2
            current_node.left = r_build(self.Node(), L, m)
            current_node.right = r_build(self.Node(), m+1, R)
            # conquer
            get_val = lambda x: x.data if x else -float('inf')  # None = -inf
            current_node.data = max(get_val(current_node.left), get_val(current_node.right))
            current_node.index=((L,R))
            return current_node
        return r_build(self.root, L, R)
            
    def query(self, _from, _to):
        # special case: empty tree
        if not self.root: return
        # special case: invalid range as input
        if _from > _to: return
        L, R = 0, len(self.v)-1
        def deep(current_node, L, R, _from, _to):
            if not current_node or _from > _to: return -float('inf')
            if _from <= L and R <= _to: return current_node.data
            m = (L+R)//2
            return max(deep(current_node.left, L, m, _from, min(m, _to)),
                        deep(current_node.right, m+1, R, max(_from, m+1), _to))
        return deep(self.root, L, R, _from, _to)

    def traverse(self):
        """traverse the tree
        """
        def deep(current_node, level):
            if not current_node: return
            deep(current_node.left, level+1)
            print('\t'*level, f'--> ({current_node.data})[{current_node.index}]')
            deep(current_node.right, level+1)
        return deep(self.root, level=0)
    
    def __repr__(self):
        self.traverse()
        return f'{self.__dict__}:'
