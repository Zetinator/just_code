"""custom implementation of a binary search tree with the purpose of practice
the ADT contains the following methods:
    - insert: insert a new node in the tree
    - search: return the node with the given value
    - delete: delete the given value from the tree
    - successor: return the next in order successor
"""
class BST():
    class Node():
        """Node basic chainable storage unit
        """
        def __init__(self, x=None):
            self.value = x
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
        def r(current_node, level=0):
            if not current_node: return
            r(current_node.left, level+1)
            res.append('\t'*level + f'-->({current_node.value})')
            r(current_node.right, level+1)
        r(self.root)
        return '\n'.join(res)

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

    def successor(self, value):
        """get the next in-order successor
        """
        if not self.root or value == None: raise ValueError(f'successor of {value} not found')
        # execute standard binary search... but keeping ranges
        def get(node, r):
            if not node: raise KeyError(f'{value} not in the tree')
            if node.value == value: return (node, r)
            if value < node.value: return get(node.left, node)
            else: return get(node.right, r)
        node, r = get(self.root, None)
        # no right subtree, return the previous bigger ancestor
        if not node.right: return r
        # go all left in the right subtree to get the successor
        node = node.right
        while node.left: node = node.left
        return node
    
    def rotate_right(self, node):
        """standard right rotation
        """
        tmp = self.Node(node.value)
        tmp.left, tmp.right = node.left.right, node.right
        # rotate...
        node.value = node.left.value
        node.left, node.right = node.left.left, tmp

    def rotate_left(self, node):
        """standard left rotation
        """
        tmp = self.Node(node.value)
        tmp.left, tmp.right = node.left, node.right.left
        # rotate...
        node.value = node.right.value
        node.left, node.right = tmp, node.right.right

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
        r(node, parent)

    def build_from_array(self, indexes):
        """build from an heap like array...
        """
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
        """method for debugging the heap-like array
        """
        def r(i, indexes, level=0):
            left = lambda: i*2 +1
            right = lambda: i*2 +2
            if left() < len(indexes): r(left(), indexes, level+1)
            if indexes[i] != -1: print('\t'*level, f'-->({indexes[i]})')
            if right() < len(indexes): r(right(), indexes, level+1)
        return r(0, indexes, level=0)
