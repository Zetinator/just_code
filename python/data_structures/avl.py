"""custom implementation of a self balanced binary search tree with the purpose of practice
the ADT contains the following methods:
    - insert
    - search
    - travese
    - delete
"""
class AVL():
    class Node():
        """Node basic chainable storage unit
        """
        def __init__(self, x=None):
            self.value = x
            self.height = 1
            self.left = None
            self.right = None

    def __init__(self, x=[]):
        self.root = None
        for e in x:
            self.insert(e)

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
            # rebalance
            height = lambda x: x.height if x else 0
            balance_factor = height(current_node.right) - height(current_node.left)
            # rotations...
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

    def __repr__(self):
        res = []
        def r(current_node, level=0):
            if not current_node: return
            r(current_node.left, level+1)
            res.append('\t'*level + f'-->({current_node.value})')
            r(current_node.right, level+1)
        r(self.root)
        return '\n'.join(res)
