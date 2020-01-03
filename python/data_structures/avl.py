"""custom implementation of a self balanced binary search tree with the purpose of practice
the ADT contains the following methods:
    - insert
    - search
    - travese
    - delete
    - successor
"""
from data_structures import bst

class AVL(bst.BST):
    class Node():
        """Node basic chainable storage unit
        """
        def __init__(self, x=None):
            self.value = x
            self.height = 1
            self.left = None
            self.right = None
        def __repr__(self):
            return repr(self.value)

    def __init__(self, x=[]):
        self.root = None
        for e in x:
            self.insert(e)

    def __repr__(self):
        res = []
        def r(node, level=0):
            if not node: return
            r(node.left, level+1)
            res.append('\t'*level + f'-->({node.value}){node.height}')
            r(node.right, level+1)
        r(self.root)
        return '\n'.join(res)

    def __len__(self):
        """depth of the tree
        """
        return self.root.height

    def rotate_left(self, pivot):
        """left rotation...
        https://en.wikipedia.org/wiki/AVL_tree#Simple_rotation
        """
        aux_node = self.Node(pivot.value)
        aux_node.left, aux_node.right = pivot.left, pivot.right.left
        # replace
        pivot.value = pivot.right.value
        pivot.left, pivot.right = aux_node, pivot.right.right
        # update weights
        self.update_weights(pivot.left)
        self.update_weights(pivot)

    def rotate_right(self, pivot):
        """right rotation...
        https://en.wikipedia.org/wiki/AVL_tree#Simple_rotation
        """
        aux_node = self.Node(pivot.value)
        aux_node.left, aux_node.right = pivot.left.right, pivot.right
        # replace
        pivot.value = pivot.left.value
        pivot.left, pivot.right = pivot.left.left, aux_node
        # update weights
        self.update_weights(pivot.right)
        self.update_weights(pivot)

    def update_weights(self, node):
        """method to compute the weights of a node given the weights of its children
        the default weight of a node is 1, and the null node is 0
        """
        height = lambda x: x.height if x else 0
        node.height = max(height(node.left), height(node.right)) + 1

    def insert(self, x):
        """insert a new node into the bst, and rebalance
        """
        # special case: empty bst
        if not self.root: self.root = self.Node(x); return
        # execute normal insertion
        def r(current_node, x):
            if current_node.value == x: raise ValueError('No duplicates allowed!')
            if x < current_node.value:
                if current_node.left:
                    r(current_node.left, x)
                else:
                    current_node.left = self.Node(x)
            else:
                if current_node.right:
                    r(current_node.right, x)
                else:
                    current_node.right = self.Node(x)
            # update the weights of each visited node
            self.update_weights(current_node)
            # rebalance violations in balance_factor with rotations...
            height = lambda x: x.height if x else 0
            balance_factor = height(current_node.right) - height(current_node.left)
            if balance_factor < -1:  # case: left
                if x > current_node.left.value:  # case: left-right
                    self.rotate_left(current_node.left)
                self.rotate_right(current_node)
                return
            if balance_factor > 1:  #case: right
                if x < current_node.right.value:  # case: right-left
                    self.rotate_right(current_node.right)
                self.rotate_left(current_node)
                return
        r(self.root, x)

    def delete(self, value):
        """search for value, and rotate until leaf, then delete
        """
        if value == None or not self.root: raise KeyError(f'{value} not found')
        # standard binary search but keep the parent
        def get(node, parent):
            if not node: raise KeyError(f'{value} not found')
            if node.value == value: return (node, parent)
            if value < node.value: return get(node.left, node)
            else: return get(node.right, node)
        node, parent = get(self.root, None)
        # bring it down to leaf... then is trivial to erase
        def r(node, parent):
            # are you root?
            if not node.left and not node.right:
                if not parent: self.root = None
                if node == parent.right: parent.right = None; return
                else: parent.left = None; return
            # rotate until leaf...
            child = node.left or node.right
            if child == node.left:
                self.rotate_right(node); r(node.right, node)
            else:
                self.rotate_left(node); r(node.left, node)
            # update weights...
            self.update_weights(node)
        r(node, parent)

    def search(self, value):
        """standard search for 'x' in the tree
        """
        if not self.root: raise ValueError(f'{value} not found')
        def r(node):
            if not node: raise ValueError(f'{value} not found')
            if value == node.value: return node
            if value < node.value: return r(node.left)
            else: return r(node.right)
        return r(self.root)
