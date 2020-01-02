"""this is the implementation of a red black tree class
https://en.wikipedia.org/wiki/Red%E2%80%93black_tree
the ADT contains the following methods:
    - insert
    - search
"""

class RBTree():
    class Node():
        """Node basic chainable storage unit
        """
        def __init__(self, value=None, color='r'):
            self.value = value
            self.left = None
            self.right = None
            self.color = color

    def __init__(self, x=[]):
        self.root = None
        for e in x:
            self.insert(e)

    def rotate_right(self, pivot):
        # take care of orphans...
        orphan = pivot.left.right
        # create replacement...
        tmp = self.Node(pivot.value)
        tmp.left, tmp.right = orphan, pivot.right
        # rotate...
        pivot.value = pivot.left.value
        pivot.left, pivot.right = pivot.left.left, tmp

    def rotate_left(self, pivot):
        # take care of orphans...
        orphan = pivot.right.left
        # create replacement...
        tmp = self.Node(pivot.value)
        tmp.left, tmp.right = pivot.left, orphan
        # rotate...
        pivot.value = pivot.right.value
        pivot.left, pivot.right = tmp, pivot.right.right

    def insert(self, value):
        if value == None: return
        # special case: empty tree
        if not self.root: self.root = self.Node(value, color='b'); return
        # perform standard bst insertion...
        def r(node, parent):
            if value == node.value: raise ValueError('No duplicates allowed...')
            if value < node.value:
                if node.left: r(node.left, node)
                else: node.left = self.Node(value)
            else:
                if node.right: r(node.right, node)
                else: node.right = self.Node(value)
            # repair violations to rb_tree's invariants... 4 special cases
            def brother(node, parent):
                if not parent: return self.Node(color='b')
                bro = parent.left if parent.right == node else parent.right
                return bro or self.Node(color='b')
            # special case 1: just make sure root remains black...
            if not parent: node.color = 'b'; return
            # special case 2: no further violations...
            elif node.color == 'b': return
            # special case 3: uncle is red -> recolor
            elif brother(node, parent).color == 'r':
                parent.color = 'r'
                node.color = brother(node, parent).color = 'b'
                return
            # special case 4: uncle is black -> rotate
            else:  # rotate right
                if parent.left == node:
                    if value > node.value:  # left -> right
                        self.rotate_left(node)
                    self.rotate_right(parent)
                
                else:  # rotate left
                    if value < node.value:  # right -> left
                        self.rotate_right(node)
                    self.rotate_left(parent)
                # switch colors parent <-> brother
                bro = brother(node, parent)
                parent.color, bro.color = bro.color, parent.color
        r(self.root, None)

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
        if not self.root: return
        res = []
        def r(node, level=0):
            if not node: return
            r(node.left, level +1)
            res.append('\t'*level + f'-->({node.value}){node.color}')
            r(node.right, level +1)
        r(self.root)
        return '\n'.join(res)

# local test...
# from random import uniform
# test = list(set([int(uniform(1, 100)) for _ in range(40)]))
# test = [2, 3, 7, 9, 10, 11, 13, 17, 18]
# test = [1, 2, 3, 11, 12, 14, 18, 19, 22, 29, 31, 33, 38, 41, 44, 51, 55, 57, 62, 63, 66, 70, 72, 73, 76, 81, 88, 90, 93, 97, 98]
# print(f'testing with: {test}')
# rbt = RBTree(test)
# print(rbt)
