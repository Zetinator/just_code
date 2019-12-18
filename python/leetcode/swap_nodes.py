"""https://www.hackerrank.com/challenges/swap-nodes-algo/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=search

Complete the swapNodes function in the editor below. It should return a two-dimensional array where each element is an array of integers representing the node indices of an in-order traversal after a swap operation.

swapNodes has the following parameter(s):
- indexes: an array of integers representing index values of each , beginning with , the first element, as the root.
- queries: an array of integers, each representing a  value.
"""
from collections import deque
import sys
sys.setrecursionlimit(3000)

class Node():
    """standard node implementation
    """
    def __init__(self, index):
        self.index = index
        self.left = None
        self.right = None

def swap(root, swap_at):
    """swap nodes at every level%swap_at == 0
    """
    # standard post traversal... 
    # because if we make the swap and then recurse weird stuff happens
    def deep(current_node, level, swap_at):
        if not current_node: return
        deep(current_node.left, level+1, swap_at)
        deep(current_node.right, level+1, swap_at)
        if (level+1)%swap_at == 0:
            current_node.left, current_node.right = current_node.right, current_node.left
    return deep(root, level=0, swap_at=swap_at)

def build_tree(indexes):
    """build tree from an array of indexes
    """
    root = Node(1)
    # we start with the root and traverse using standard BFS
    queue = deque()
    queue.append(root)
    for i_l, i_r in indexes:
        node = queue.popleft()
        if i_l != -1:
            node.left = Node(i_l)
            queue.append(node.left)
        if i_r != -1:
            node.right = Node(i_r)
            queue.append(node.right)
    return root

def swapNodes(indexes, queries):
    """main method...
    """
    # we build the tree, from the given list of indexes
    root = build_tree(indexes)
    # standard method to traverse the tree (in-order)
    def traverse(root):
        res = []
        def deep(current_node, level):
            if not current_node: return
            deep(current_node.left, level+1)
            res.append(current_node.index)
            deep(current_node.right, level+1)
        deep(root, level=0)
        return res
    # do the swaps, and keep the global result here in 'output'
    output = []
    for q in queries:
        # in 'res' we keep the result of every swap operation
        swap(root, q)
        output.append(traverse(root))
    return output

# test
indexes = [[2, 3],
        [-1, 4],
        [-1, 5],
        [-1, -1],
        [-1, -1]]

indexes = [[2, 3],
        [4, -1],
        [5, -1],
        [6, -1],
        [7, 8],
        [-1, 9],
        [-1, -1],
        [10, 11],
        [-1, -1],
        [-1, -1],
        [-1, -1]]

queries = [2, 4]
print(f'testing with: {indexes}')
print(f'ans: {swapNodes(indexes, queries)}')
