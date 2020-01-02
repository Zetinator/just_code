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
            self.value = x
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
            return
        return r(self.root, x)

    def search(self, x):
        """search for 'x' in the tree
        """
        def r(current_node, x):
            if not current_node: raise ValueError(f'{x} not in the tree')
            if current_node.value == x: return current_node
            if x < current_node.value:
                return r(current_node.left, x)
            else:
                return r(current_node.right, x)
        return r(self.root, x)

    def traverse(self):
        """traverse the tree
        """
        def r(current_node, level):
            if not current_node: return
            r(current_node.left, level+1)
            print('\t'*level, f'--> ({current_node.value})')
            r(current_node.right, level+1)
        return r(self.root, level=0)
    
    def __repr__(self):
        res = []
        def r(current_node, level=0):
            if not current_node: return
            r(current_node.left, level+1)
            res.append('\t'*level + f'-->({current_node.value})')
            r(current_node.right, level+1)
        r(self.root)
        return '\n'.join(res)
    
    def retrieve_successor(self, node):
        # first some pruning
        if not node: return
        if not node.right: return
        def r(parent, current_node, righteous=1):  # comes from the right side of the parent
            if not current_node.left:  # found it
                if righteous:
                    if current_node.right: parent.right = current_node.right
                    if not current_node.right: parent.right = None
                else:
                    if current_node.right: parent.left = current_node.right
                    if not current_node.right: parent.left = None
                return current_node
            return r(current_node, current_node.left, 0)
        return r(node, node.right, 1)

    def delete(self, v):
        """search and delete 'x' in the tree
        More complicated than what I thought
        """
        def r(v, parent, current_node, righteous=1):
            if not current_node: return False
            if current_node.value == v:
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
                    current_node.value = tmp_node.value
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
            if v < current_node.value:
                return r(v, current_node, current_node.left, 0)
            else:
                return r(v, current_node, current_node.right, 1)
        if not r(v, None, self.root): raise KeyError(f'{v} is not in the tree, nothing to remove')
        return True

    def build_from_array(self, indexes):
        root = self.root
        def build(node, i, indexes, level=0):
            # aux functions
            left = lambda: i*2 +1
            right = lambda: i*2 +2
            # actual tree traversal
            if left() < len(indexes) and indexes[left()] != -1:
                left_node = Node(indexes[left()])
                node.left = left_node
                build(left_node, left(), indexes, level+1)
            if right() < len(indexes) and indexes[right()] != -1:
                right_node = Node(indexes[right()])
                node.right = right_node
                build(right_node, right(), indexes, level+1)
        build(root, 0, indexes, 0)
        return root

    def traverse_array(self, indexes):
        def r(i, indexes, level=0):
            left = lambda: i*2 +1
            right = lambda: i*2 +2
            if left() < len(indexes): r(left(), indexes, level+1)
            if indexes[i] != -1: print('\t'*level, f'-->({indexes[i]})')
            if right() < len(indexes): r(right(), indexes, level+1)
        return r(0, indexes, level=0)
