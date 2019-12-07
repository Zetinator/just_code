class AVL():
    def __init__(self):
        self.root = None

    class node():
        def __init__(self, v=None):
            self.value = v
            self.left = None
            self.right = None
            self.height = 1

    def traverse(self, node=None):
        def deep(current_node, level):
            if not current_node: return
            deep(current_node.left, level+1)
            height = lambda node: node.height if node else 0
            balance_factor = height(current_node.left) - height(current_node.right)
            print('current_node: value:{0:<5} level:{1:<5} weight:{2:<5} balance:{3:>3}'\
                        .format(current_node.value,
                                level,
                                current_node.height,
                                balance_factor
                                ))
            deep(current_node.right, level+1)
        return deep(self.root, 0)

    def search(self, v):
        def deep(v, current_node):
            if not current_node: return None
            if v == current_node.value: return current_node
            if v < current_node.value:
                return deep(v, current_node.left)
            else:
                return deep(v, current_node.right)
        node = deep(v, self.root)
        if not node: raise ValueError(f'{v} not in the tree')
        return node

    def get_balance_factor(self, node):
        height = lambda node: node.height if node else 0
        return height(node.right) - height(node.left)

    def update_weights(self, node):
        height = lambda node: node.height if node else 0
        node.height = max(height(node.left), height(node.right)) + 1
        return node.height

    def rotate_r(self, node):
        # tmp node
        aux_node = self.node(node.value)
        aux_node.left, aux_node.right = node.left.right, node.right
        # rotate on "node" pivot
        node.value = node.left.value
        node.left, node.right = node.left.left, aux_node
        # update heights
        self.update_weights(node.right)
        self.update_weights(node)
        return node

    def rotate_l(self, node):
        # tmp node
        aux_node = self.node(node.value)
        aux_node.left, aux_node.right = node.left, node.right.left
        # rotate on "node" pivot
        node.value = node.right.value
        node.left, node.right = aux_node, node.right.right
        # update heights
        self.update_weights(node.left)
        self.update_weights(node)
        return node


    def insert(self, v):
        print(f'inserting: {v}')
        def deep(v, current_node):
            # are you root?
            if not current_node: self.root = self.node(v); return
            # no duplicates!
            if v == current_node.value: raise ValueError('not duplicates allowed')
            # insert as you would...
            if v < current_node.value:
                if current_node.left:
                    deep(v, current_node.left)
                else:
                    current_node.left = self.node(v)
            else:
                if current_node.right:
                    deep(v, current_node.right)
                else:
                    current_node.right = self.node(v)
            # rebalance...
            self.update_weights(current_node)
            bf = self.get_balance_factor(current_node)
            if bf < -1:  # case left
                if v > current_node.left.value:  # case left-right
                    current_node.left = self.rotate_l(current_node.left)
                self.rotate_r(current_node)
                return
            if bf > 1:  # case right
                if v < current_node.right.value:  # case right-left
                    current_node.right = self.rotate_r(current_node.right)
                self.rotate_l(current_node)
                return
        deep(v, self.root)
        return self.traverse(self.root)

# test
test = [33, 66, 1, 65, 5, 7, 41, 74, 11, 45, 14, 60, 48, 84, 85, 31, 93, 63]
print(f'testing with: {test}')
tree = AVL()
for e in test: tree.insert(e)
