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
            self.data = x
            self.height = 1
            self.left = None
            self.right = None

    def __init__(self, x=None):
        self.root = None
        if x:
            for e in x:
                self.insert(e)

    def rotate_left(self, pivot):
        """left rotation...
        https://en.wikipedia.org/wiki/AVL_tree#Simple_rotation
        """
        aux_node = self.Node(pivot.data)
        aux_node.left, aux_node.right = pivot.left, pivot.right.left
        # replace
        pivot.data = pivot.right.data
        pivot.left, pivot.right = aux_node, pivot.right.right
        # update weights
        self.update_weights(pivot.left)
        self.update_weights(pivot)

    def rotate_right(self, pivot):
        """right rotation...
        https://en.wikipedia.org/wiki/AVL_tree#Simple_rotation
        """
        aux_node = self.Node(pivot.data)
        aux_node.left, aux_node.right = pivot.left.right, pivot.right
        # replace
        pivot.data = pivot.left.data
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
        def deep(current_node, x):
            if current_node.data == x: raise ValueError('No duplicates allowed!')
            if x < current_node.data:
                if current_node.left:
                    deep(current_node.left, x)
                else:
                    current_node.left = self.Node(x)
            else:
                if current_node.right:
                    deep(current_node.right, x)
                else:
                    current_node.right = self.Node(x)
            # update the weights of each visited node
            self.update_weights(current_node)
            # rebalance
            height = lambda x: x.height if x else 0
            balance_factor = height(current_node.right) - height(current_node.left)
            # rotations...
            if balance_factor < -1:  # case: left
                if x > current_node.left.data:  # case: left-right
                    self.rotate_left(current_node.left)
                self.rotate_right(current_node)
                return
            if balance_factor > 1:  #case: right
                if x < current_node.right.data:  # case: right-left
                    self.rotate_right(current_node.right)
                self.rotate_left(current_node)
                return
        deep(self.root, x)

    def search(self, x):
        """standard search for 'x' in the tree
        """
        def deep(current_node, x):
            if not current_node: raise ValueError(f'{x} not in the tree')
            if current_node.data == x: return current_node
            if x < current_node.data:
                return deep(current_node.left, x)
            else:
                return deep(current_node.right, x)
        return deep(self.root, x)

    def traverse(self):
        """traverse the tree
        """
        def deep(current_node, level):
            if not current_node: return
            deep(current_node.left, level+1)
            print('\t'*level, f'--> ({current_node.data})')
            deep(current_node.right, level+1)
        return deep(self.root, level=0)
    
    def __repr__(self):
        self.traverse()
        return f'{self.__dict__}:'
    
# test the implementation:
test = [33, 66, 1, 65, 5, 7, 41, 74, 11, 45, 14, 60, 48, 84, 85, 31, 93, 63]
print(f'testing with: {test}')
tree = AVL(test)
tree.traverse()



