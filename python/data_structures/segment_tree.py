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
        def __init__(self, data=None):
            self.data = None
            self.left = None
            self.right = None

    def __init__(self, v):
        self.root = self.Node((0, len(v)))
        self.v = v
        self.build(v)

    def build(self, v):
        if not v: return
        def r_build(_from, _to, current_node):
            print(f'STATUS: from: {_from}, to: {_to}, v: {self.v[_from:_to]}')
            # base case: empty interval
            if not self.v[_from:_to]: return
            # base case: just one element in the interval
            if len(self.v[_from:_to]) == 1:
                current_node.data = self.v[_from:_to]
                return
            # divide
            m =-(-_to//2)  # integer division + ceil
            if self.v[_from:m]:
                print('left')
                current_node.left = self.Node()
                r_build(_from, m, current_node.left)
            if self.v[m:_to]:
                print('right')
                current_node.right = self.Node()
                r_build(m, _to, current_node.right)
            # conquer
            get_val = lambda x: x.data if x else -float('inf')
            current_node.data = max(get_val(current_node.left), get_val(current_node.right))
        return r_build(0, len(self.v), self.root)
            
    def traverse(self):
        """traverse the tree
        """
        def deep(current_node):
            if not current_node: return
            deep(current_node.left)
            print(f'{current_node.data}')
            deep(current_node.right)
        return deep(self.root)
    
# test
test = ST([3,5,4,1,6,0,9])
print(f'test:')
