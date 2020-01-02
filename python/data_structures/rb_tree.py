"""this is the implementation of a red black tree class
https://en.wikipedia.org/wiki/Red%E2%80%93black_tree
the ADT contains the following methods:
    - insert
    - build
    - search
"""

class RBTree():
    class Node():
        def __init__(self, data=None, color='r'):
            self.data = data
            self.left = None
            self.right = None
            self.color = color

        def __repr__(self):
            return repr(self.data)

    def __init__(self, x=[]):
        self.root = None
        for e in x:
            self.insert(e)

    def rotate_right(self, pivot):
        # take care of orphans...
        orphan = pivot.left.right
        # create replacement...
        tmp = self.Node(pivot.data)
        tmp.left, tmp.right = orphan, pivot.right
        # rotate...
        pivot.data = pivot.left.data
        pivot.left, pivot.right = pivot.left.left, tmp

    def rotate_left(self, pivot):
        # take care of orphans...
        orphan = pivot.right.left
        # create replacement...
        tmp = self.Node(pivot.data)
        tmp.left, tmp.right = pivot.left, orphan
        # rotate...
        pivot.data = pivot.right.data
        pivot.left, pivot.right = tmp, pivot.right.right

    def insert(self, data):
        if data == None: return
        # perform standard bst insertion...
        if not self.root: self.root = self.Node(data, color='b'); return
        def r(node, parent):
            print(f'inserting: {data}, current_node: {node}, parent: {parent}')
            if data == node.data: raise ValueError('No duplicates allowed...')
            if data < node.data:
                if node.left: r(node.left, node)
                else: node.left = self.Node(data)
            else:
                if node.right: r(node.right, node)
                else: node.right = self.Node(data)
            # repair violations to rb_tree's invariants... 4 special cases
            def brother(node, parent):
                if not parent: return self.Node(color='b')
                bro = parent.left if parent.right == node else parent.right
                return bro or self.Node(color='b')
            # special case 1: just make sure root remains black...
            if not parent: node.color = 'b'; print('case 1: root'); return
            # special case 2: no further violations...
            elif node.color == 'b': print(f'case 2: normal'); return
            # special case 3: uncle is red -> recoloring
            elif brother(node, parent).color == 'r':
                print(f'case 3: recolor')
                parent.color = 'r'
                node.color = brother(node, parent).color = 'b'
                return
            # special case 4: uncle is black -> rotate
            else:
                print(f'case 4: rotate')
                # rotate right
                if parent.left == node:
                    print('rotate right')
                    # left -> right
                    if data > node.data:
                        print('left -> right')
                        self.rotate_left(node)
                    self.rotate_right(parent)
                # rotate left
                else:
                    print('rotate left')
                    # right -> left
                    if data < node.data:
                        print('rotate left')
                        self.rotate_right(node)
                    self.rotate_left(parent)
                # switch colors parent <-> brother
                bro = brother(node, parent)
                parent.color, bro.color = bro.color, parent.color
        r(self.root, None)

    def __repr__(self):
        if not self.root: return
        res = []
        def r(node, level=0):
            if not node: return
            r(node.left, level +1)
            res.append('\t'*level + f'-->({node.data}){node.color}')
            r(node.right, level +1)
        r(self.root)
        return '\n'.join(res)

from random import uniform
test = list(set([int(uniform(1, 20)) for _ in range(30)]))
test = [2, 3, 7, 9, 10, 11, 13, 17, 18]
test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19]
rbt = RBTree(test)
