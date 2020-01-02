"""https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=trees&h_r=next-challenge&h_v=zen

You are given pointer to the root of the binary search tree and two values  and . You need to return the lowest common ancestor (LCA) of  and  in the binary search tree.
"""

class BST():
    class Node():
        """Node basic chainable storage unit
        """
        def __init__(self, x=None):
            self.info = x
            self.left = None
            self.right = None

    def __init__(self, x=[]):
        self.root = None
        for e in x:
            self.insert(e)

    def insert(self, x):
        """insert a new node into the bst
        """
        # special case: empty bst
        if not self.root: self.root = self.Node(x); return
        # general case
        def deep(current_node, x):
            if current_node.info == x: raise ValueError('No duplicates allowed!')
            if x < current_node.info:
                if current_node.left:
                    deep(current_node.left, x)
                else:
                    current_node.left = self.Node(x)
            else:
                if current_node.right:
                    deep(current_node.right, x)
                else:
                    current_node.right = self.Node(x)
            return
        return deep(self.root, x)

    def __repr__(self):
        ans = []
        def deep(current_node, level):
            if not current_node: return
            deep(current_node.left, level+1)
            ans.append('\t'*level)
            ans.append(f'-->({current_node.info})\n')
            deep(current_node.right, level+1)
        deep(self.root, level=0)
        return ''.join(ans)

def lca(root, v1, v2):
    """almost there...
    """
    v = [v1, v2]
    def r(node, parent, level=0):
        if not node: return (float('inf'), parent)
        if node.info == v[0] or node.info == v[1]: return (level-1, parent)
        return min(r(node.left, node, level+1), r(node.right, node, level+1), key= lambda x: x[0])
    return min(r(root.left, root, 0), r(root.right, root, 0), key=lambda x: x[0])[1] or root

def lca(root, v1, v2):
    """iterative approach
    very clever...
    """
    current_node = root
    while True:
        if current_node.info > v1 and current_node.info > v2:
            current_node=current_node.left
        elif current_node.info < v1 and current_node.info < v2:
            current_node=current_node.right
        else:
            return current_node
# test
test = """8 4 2 1 3 6 5 7 10 14 15 9 12 11 13"""
v1, v2 = 15, 11
test = """4 2 3 1 7 6"""
v1, v2 = 1, 7
test = [int(n) for n in test.split()]
bst = BST(test)
print(f'ans: {lca(bst.root, v1, v2).info}')

