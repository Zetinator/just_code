"""
node based binary tree, homemade...
"""
class bt():
    def __init__(self):
        self.root = None

    class node():
        def __init__(self, v, left=None, right=None):
            self.value = v
            self.left = left
            self.right = right

    def traverse(self):
        def deep(current_node, n):
            if not current_node: return
            deep(current_node.left, n+1)
            print(f'current_node: value:{current_node.value}, n:{n}')
            deep(current_node.right, n+1)
        return deep(self.root, 0)

    def max_depth(self):
        def deep(current_node, n):
            if not current_node: return n
            return max(deep(current_node.left, n+1), deep(current_node.right, n+1))
        return deep(self.root, 0)

    def min_depth(self):
        def deep(current_node, n):
            if not current_node: return n
            return min(deep(current_node.left, n+1), deep(current_node.right, n+1))
        return deep(self.root, 0)

    def search(self, v):
        def deep(current_node):
            if not current_node: return False
            if current_node.value == v: return True
            return deep(current_node.left) or deep(current_node.right)
        if not deep(self.root): raise ValueError(f'{v} is not in the tree')
        return True

    def insert(self, v):
        if not self.root:  # empty tree
            self.root = self.node(v)
            return
        def deep(v, current_node):
            if v == current_node.value: raise ValueError('No duplicates allowed!')
            if v < current_node.value:
                if not current_node.left:
                    current_node.left = self.node(v)
                    return
                else: return deep(v, current_node.left)
            else:
                if not current_node.right:
                    current_node.right = self.node(v)
                    return
                else: return deep(v, current_node.right)
        return deep(v, self.root)

    def find_successor(self, node):
        print('looking...')
        if not node: return
        def deep(current_node):
            if not current_node.left: return current_node
            return deep(current_node.left)
        if not node.right: return
        return deep(node.right)

    def delete(self, v):
        def deep(v, parent, current_node):
            if not current_node: return False
            print(f'STATUS: searching for: {v}, current_node: {current_node.value}')
            if current_node.value == v:
                # case: no children --> set None
                if not current_node.left and not current_node.right:
                    print('no children...')
                    if not parent:
                        self.root = None
                        return True
                    if current_node.value > parent.value:
                        parent.right = None
                    else:
                        parent.left = None
                    return True
                # case: 2 children --> replace with successor
                if current_node.left and current_node.right:
                    print(f'two children... look for successor...')
                    if not parent:
                        tmp = self.find_successor(current_node)
                        tmp.left, tmp.right = current_node.left, current_node.right
                        self.delete(tmp.value)
                        self.root = tmp
                        return True
                    if current_node.value > parent.value:
                        tmp = self.find_successor(current_node)
                        tmp.left, tmp.right = current_node.left, current_node.right
                        self.delete(tmp.value)
                        parent.right = tmp
                    else:
                        tmp = self.find_successor(current_node)
                        tmp.left, tmp.right = current_node.left, current_node.right
                        self.delete(tmp.value)
                        parent.left = tmp
                    return True
                # case: one children --> bypass
                if current_node.left or current_node.right:
                    print(f'one children... bypassing...')
                    if not parent:
                        self.root = current_node.left or current_node.right
                        return True
                    if current_node.value > parent.value:
                        parent.right = current_node.left or current_node.right
                    else:
                        parent.left = current_node.left or current_node.right
                    return True
            # sorry mate... keep looking
            return deep(v, current_node, current_node.left) or \
                   deep(v, current_node, current_node.right)
        if not deep(v, None, self.root): raise KeyError(f'{v} is not in the tree, nothing to remove')
        return True

                    

# test
test = [3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]
print(f'testing with: {test}')
tree = bt()
for e in test: tree.insert(e)
