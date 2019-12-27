"""https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=trees&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

Given the root node of a binary tree, determine if it is a binary search tree.
"""

def checkBST(root):
    """take into consideration the possible intervals
    """
    def r(node, left, right):
        if not node: return True
        if node.data <= left or node.data >= right: return False
        return r(node.left, left, node.data) and r(node.right, node.data, right)
    return r(root, -float('inf'), float('inf'))

def traverse(root):
    """traverse the tree
    """
    def deep(current_node, level):
        if not current_node: return
        deep(current_node.left, level+1)
        print('\t'*level, f'--> ({current_node.data})')
        deep(current_node.right, level+1)
    return deep(root, level=0)

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = node(3)
root.right = node(6)
root.left = node(2)
root.right.left = node(5)
root.right.right = node(7)
root.left.left = node(1)
root.left.right = node(4)

traverse(root)
print(f'ans: {checkBST(root)}')
