"""this is the implementation of a red black tree class
https://en.wikipedia.org/wiki/Red%E2%80%93black_tree
the ADT contains the following methods:
    - insert
    - build
    - search
"""

class RBTree():
    class Node():
        def __init__(self, data=None, parent= None, color='r'):
            self.data = data
            self.parent = parent
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
        tmp = self.Node(pivot.data)
        tmp.left, tmp.right = orphan, pivot.right
        tmp.left.parent = tmp.right.parent = tmp
        # rotate...
        pivot.data = pivot.left.data
        pivot.left, pivot.right = pivot.left.left, tmp
        pivot.left.parent = pivot.right.parent = pivot

    def rotate_left(self, pivot):
        # take care of orphans...
        orphan = pivot.right.left
        # create replacement...
        tmp = self.Node(pivot.data)
        tmp.left, tmp.right = pivot.left, orphan
        tmp.left.parent = tmp.right.parent = tmp
        # rotate...
        pivot.value = pivot.right.value
        pivot.left, pivot.right = tmp, pivot.right.right
        pivot.left.parent = pivot.right.parent = pivot

    def insert(self, data):
        if data == None: return
        # perform standard bst insertion...
        if not self.root: self.root = self.Node(data, color='b'); return
        def r(node):
            if data == node.data: raise ValueError('No duplicates allowed...')
            if data < node.data:
                if node.left: r(node.left)
                else: node.left = self.Node(data, node)
            else:
                if node.right: r(node.right)
                else: node.right = self.Node(data, node)
            print(f'inserting: {data}, visiting... {node.data}')
            # repair violations to rb_tree's invariants... 4 special cases
            def grandpa(node):
                if not node.parent: return
                return node.parent.parent
            def brother(node):
                if not node.parent: return self.Node(color='b')
                bro = node.parent.left if node.parent.right == node else node.parent.right
                return bro or self.Node(color='b')
            def uncle(node):
                if not node.parent and not node.parent.parent: return self.Node(color='b')
                return brother(node.parent) or self.Node(color='b')
            # special case 1: just make sure root remains black...
            if not node.parent: node.color = 'b'; print('case:1'); return
            # special case 2: no further violations...
            elif node.parent.color == 'b': print(f'case: 2'); return
            # special case 3: uncle is red -> recoloring
            elif uncle(node).color == 'r':
                print(f'case 3')
                _uncle = uncle(node)
                grandparent = grandpa(node)
                grandparent.color = 'r'
                node.parent.color = uncle.color = 'b'
                return
            # special case 4: uncle is black -> rotate
            # if uncle(node).color == 'b':
            else:
                print(f'case 4')
                parent, grandparent = node.parent, grandpa(node)
                # rotate right
                if node == parent.left:
                    print(f'rotate right')
                    # left -> right
                    if parent == grandparent.left:
                        print(f'left -> right')
                        self.rotate_left(parent)
                    self.rotate_right(grandparent)
                # rotate left
                if node == parent.right:
                    print(f'rotate left')
                    # right -> left
                    if parent == grandparent.right:
                        print(f'right - left')
                        self.rotate_right(parent)
                    self.rotate_left(parent)
                # switch colors parent <-> brother
                _brother = brother(node)
                node.parent.color, _brother.color = _brother.color, node.parent.color
        r(self.root)

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

# from random import uniform
# test = list(set([int(uniform(1, 20)) for _ in range(15)]))
test = [2, 3, 7, 9, 10, 11, 13, 17, 18]
rbt = RBTree(test)
