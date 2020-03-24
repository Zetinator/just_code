"""https://www.hackerrank.com/challenges/tree-level-order-traversal/problem
You are given a pointer to the root of a binary tree. You need to print the level order traversal of this tree. In level order traversal, we visit the nodes level by level from left to right. You only have to complete the function. For example:
     1
      \
       2
        \
         5
        /  \
       3    6
        \
         4  
For the above tree, the level order traversal is 1 -> 2 -> 5 -> 3 -> 6 -> 4.
"""
class BST():
    class Node():
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
    def __init__(self, x=[]):
        self.root = None
        for e in x: self.insert(e)
    def __repr__(self):
        res = []
        def traverse(node, level=0):
            if not node: return
            traverse(node.right, level+1)
            res.append('\t'*level + f'-->({node.value})')
            traverse(node.left, level+1)
        traverse(self.root)
        return '\n'.join(res)

    def insert(self, value):
        if not self.root: self.root = self.Node(value); return
        def r(node, value):
            if not node or node.value == value: return
            if value < node.value:
                if node.left: return r(node.left, value)
                else: node.left = self.Node(value)
            else:
                if node.right: return r(node.right, value)
                else: node.right = self.Node(value)
        return r(self.root, value)

def level_traversal(bst: BST)-> list:
    if not bst.root: return
    res = {}
    def traverse(node, level=0):
        if not node: return
        traverse(node.left, level+1)
        res.setdefault(level, []).append(node.value)
        traverse(node.right, level+1)
    traverse(bst.root)
    tmp = []
    for i in range(len(res)):
        tmp += res[i]
    return tmp

# test
init = [9,4,14,2,7,12,17]
bst = BST(init)
print(f'bst: \n{bst}\n')
print(f'print level order: {level_traversal(bst)}')
