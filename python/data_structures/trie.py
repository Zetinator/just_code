"""custom implementation of a trie with the purpose of practice
the ADT contains the following methods:
    - insert
    - search
    - delete
"""
class Trie():
    class Node():
        """Node basic chainable storage unit
        """
        def __init__(self, x=None):
            self.data = x
            self.children = {}

    def __init__(self, x=None):
        self.root = self.Node()
        if x:
            for key in x:
                self.insert(key)

    def __repr__(self):
        nodes = []
        def r(node, level):
            if node.data != None:
                nodes.append('\t'*(level-1) + f'({node.data})\n')
            for k,child in node.children.items():
                nodes.append('\t'*level + f'--<{k}>--\n')
                r(child, level+1)
        r(self.root, 0)
        return ''.join(nodes)

    def insert(self, key):
        """insert a new key
        """
        current_node = self.root
        for letter in key:
            if letter not in current_node.children:
                current_node.children[letter] = self.Node()
            current_node = current_node.children[letter]
        current_node.data = key

    def predict(self, word=None):
        if not word or not self.root.children: return []
        res = []
        current_node = self.root
        for letter in word:
            if letter in current_node.children:
                current_node = current_node.children[letter]
        def deep(node):
            if node.data != None: return res.append(node.data)
            for key, data in node.children.items(): deep(data)
        deep(current_node)
        return res

    def search(self, key):
        current_node = self.root
        for letter in key:
            if letter not in current_node.children:
                raise ValueError(f'{key} not found')
            current_node = current_node.children[letter]
        return current_node.data
