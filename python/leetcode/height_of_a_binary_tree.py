"""https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=trees

The height of a binary tree is the number of edges between the tree's root and its furthest leaf.
"""

class BST():
    class Node():
        """Node basic chainable storage unit
        """
        def __init__(self, x=None):
            self.value = x
            self.left = None
            self.right = None

    def __init__(self, x=None):
        self.root = None
        if x:
            for e in x:
                self.insert(e)

    def insert(self, x):
        """insert a new node into the bst
        """
        # special case: empty bst
        if not self.root: self.root = self.Node(x); return
        # general case
        def deep(current_node, x):
            if current_node.value == x: raise ValueError('No duplicates allowed!')
            if x < current_node.value:
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

def height(root):
    """recursive solution...
    """
    def r(node, ans=0):
        if not node: return ans
        return max(r(node.left, ans+1), r(node.right, ans+1))
    return r(root)

# test
test = [e for e in range(10)]
print(f'test with: {test}')
bst = BST(test)
print(f'ans: {height(bst.root)}')
