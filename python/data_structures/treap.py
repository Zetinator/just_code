"""this is the implementation of a treap class
https://en.wikipedia.org/wiki/Treap
the ADT contains the following methods:
    - insert
    - search
    - delete
"""
from data_structures import bst
from random import uniform

class Treap(bst.BST):
    class Node():
        """Node basic chainable storage unit
        """
        def __init__(self, value=None):
            self.value = value
            self.priority = uniform(0,1)
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
        tmp.priority = node.priority
        tmp.left, tmp.right = node.left.right, node.right
        # rotate...
        node.value, node.priority = node.left.value, node.left.priority
        node.left, node.right = node.left.left, tmp

    def rotate_left(self, node):
        """left rotation...
        https://en.wikipedia.org/wiki/AVL_tree#Simple_rotation
        """
        tmp = self.Node(node.value)
        tmp.priority = node.priority
        tmp.left, tmp.right = node.left, node.right.left
        # rotate...
        node.value, node.priority = node.right.value, node.right.priority
        node.left, node.right = tmp, node.right.right

    def insert(self, value):
        """insert a new node with the given value in the tree
        standard bst insertion + rotations to keep the heap invariance
        """
        if value == None: return
        if not self.root: self.root = self.Node(value); return
        # execute standard bst insertion...
        def r(node):
            if value == node.value: raise ValueError(f'No duplicates allowed...')
            if value < node.value:
                if node.left: r(node.left)
                else: node.left = self.Node(value)
            else:
                if node.right: r(node.right)
                else: node.right = self.Node(value)
            # repair max_heap invariants...
            if value > node.value:
                if node.right.priority > node.priority:
                    self.rotate_left(node)
            else:
                if node.left.priority > node.priority:
                    self.rotate_right(node)
        r(self.root)

    def delete(self, value):
        """search and delete the node with the given value in the tree
        rotate the node to be deleted with the max child until if becomes a leaf
        then just erase the leaf...
        """
        if value == None: return
        # standard binary search for the node, and the parent
        if not self.root: raise ValueError(f'{value} not found')
        def get(node, parent):
            if not node: raise ValueError(f'{value} not found')
            if value == node.value: return (node, parent)
            if value < node.value: return get(node.left, node)
            else: return get(node.right, node)
        node, parent = get(self.root, None)
        # make it a leaf so we can get rid of it easily
        def r(node, parent):
            # base case: node is a leaf
            if not node.left and not node.right:
                # are you root?
                if not parent: self.root = None; return
                if parent.right == node: parent.right = None; return
                else: parent.left = None; return
            # rotate with max_child, until no childs remain...
            priority = lambda node: node.priority if node else -float('inf')
            max_child = max(node.left, node.right, key=lambda node: priority(node))
            if max_child == node.right:
                self.rotate_left(node)
                return r(node.left, node)
            else:
                self.rotate_right(node)
                return r(node.right, node)
        return r(node, parent)
    
    def search(self, value):
        """standard binary search in the tree
        """
        if not self.root: raise ValueError(f'{value} not found')
        def r(node):
            if not node: raise ValueError(f'{value} not found')
            if value == node.value: return node
            if value < node.value: return r(node.left)
            else: return r(node.right)
        return r(self.root)

    def __repr__(self):
        if not self.root: return
        res = []
        def r(node, level=0):
            if not node: return
            r(node.left, level +1)
            res.append('\t'*level + f'-->({node.value}){node.priority:0.04}')
            r(node.right, level +1)
        r(self.root)
        return '\n'.join(res)
