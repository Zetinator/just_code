"""this is the implementation of a splay tree class
https://en.wikipedia.org/wiki/Splay_tree
the ADT contains the following methods:
    - insert
    - search
    - delete
"""
from data_structures import bst

class SplayTree(bst.BST):
    class Node():
        """Node basic chainable storage unit
        """
        def __init__(self, value=None):
            self.value = value
            self.left = None
            self.right = None
        def __repr__(self):
            return repr(self.value)

    def __init__(self, x=[]):
        self.root = None
        for e in x:
            self.insert(e)

    def rotate_right(self, node):
        """right rotation...
        https://en.wikipedia.org/wiki/AVL_tree#Simple_rotation
        """
        tmp = self.Node(node.value)
        tmp.left, tmp.right = node.left.right, node.right
        # rotate...
        node.value = node.left.value
        node.left, node.right = node.left.left, tmp

    def rotate_left(self, node):
        """left rotation...
        https://en.wikipedia.org/wiki/AVL_tree#Simple_rotation
        """
        tmp = self.Node(node.value)
        tmp.left, tmp.right = node.left, node.right.left
        # rotate...
        node.value = node.right.value
        node.left, node.right = tmp, node.right.right

    def insert(self, value):
        """insert a new node with the given value in the tree
        standard bst insertion + rotations to bring the inserted node to root
        """
        if value == None: return
        if not self.root: self.root = self.Node(value); return
        # execute standard bst insertion, but making the inserted node root
        def r(node):
            if value == node.value: raise ValueError(f'No duplicates allowed...')
            if value < node.value:
                if node.left: r(node.left)
                else: node.left = self.Node(value)
                self.rotate_right(node)
            else:
                if node.right: r(node.right)
                else: node.right = self.Node(value)
                self.rotate_left(node)
        r(self.root)

    def search(self, value):
        """standard binary search in the tree
        alike insertion, search also brings the searched node to root
        """
        if not self.root: raise ValueError(f'{value} not found')
        def r(node):
            if not node: raise ValueError(f'{value} not found')
            if value == node.value: return
            if value < node.value:
                r(node.left)
                self.rotate_right(node)
            else:
                r(node.right)
                self.rotate_left(node)
        r(self.root)
        return self.root

    def __repr__(self):
        if not self.root: return
        res = []
        def r(node, level=0):
            if not node: return
            r(node.left, level +1)
            res.append('\t'*level + f'-->({node.value})')
            r(node.right, level +1)
        r(self.root)
        return '\n'.join(res)
