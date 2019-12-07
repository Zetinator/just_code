"""custom implementation of a binary search tree with the purpose of practice
the ADT contains the following methods:
    - insert
    - search
    - delete
    - traverse
"""
class BST():
    class Node():
        """Node basic chainable storage unit
        """
        def __init__(self, x=None):
            self.data = x
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
            return
        return deep(self.root, x)

    def search(self, x):
        """search for 'x' in the tree
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
        def deep(current_node):
            if not current_node: return
            deep(current_node.left)
            print(f'{current_node.data}')
            deep(current_node.right)
        return deep(self.root)
    
    def retrieve_successor(self, node):
        # first some pruning
        if not node: return
        if not node.right: return
        def deep(parent, current_node, righteous=1):  # comes from the right side of the parent
            if not current_node.left:  # found it
                if righteous:
                    if current_node.right: parent.right = current_node.right
                    if not current_node.right: parent.right = None
                else:
                    if current_node.right: parent.left = current_node.right
                    if not current_node.right: parent.left = None
                return current_node
            return deep(current_node, current_node.left, 0)
        return deep(node, node.right, 1)

    def delete(self, v):
        """search and delete 'x' in the tree
        More complicated than what I thought
        """
        def deep(v, parent, current_node, righteous=1):
            if not current_node: return False
            if current_node.data == v:
                # case: no children --> set None
                if not current_node.left and not current_node.right:
                    if not parent:  # are you root?
                        self.root = None
                        return True
                    if righteous:
                        parent.right = None
                    else:
                        parent.left = None
                    return True
                # case: 2 children --> replace with successor
                if current_node.left and current_node.right:
                    tmp_node = self.retrieve_successor(current_node)
                    current_node.data = tmp_node.data
                    return True
                # case: one children --> bypass
                if current_node.left or current_node.right:
                    if not parent: # are you root?
                        self.root = current_node.left or current_node.right
                        return True
                    if righteous:
                        parent.right = current_node.left or current_node.right
                    else:
                        parent.left = current_node.left or current_node.right
                    return True
            # sorry mate... keep looking
            if v < current_node.data:
                return deep(v, current_node, current_node.left, 0)
            else:
                return deep(v, current_node, current_node.right, 1)
        if not deep(v, None, self.root): raise KeyError(f'{v} is not in the tree, nothing to remove')
        return True

# test
test = BST([3,5,4,1,6,0,9])
print(f'test:')
