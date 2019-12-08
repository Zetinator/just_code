"""custom implementation of a trie with the purpose of practice
the ADT contains the following methods:
    - insert
    - search
    - travese
    - delete
"""
class Trie():
    class Node():
        """Node basic chainable storage unit
        """
        def __init__(self, x=None):
            self.value = x
            self.children = {}

    def __init__(self, x=None):
        self.root = self.Node()
        if x:
            for key in x:
                self.insert(key)

    def insert(self, key):
        current_node = self.root
        for letter in key:
            if letter not in current_node.children:
                current_node.children[letter] = self.Node()
            current_node = current_node.children[letter]
        current_node.value = key

    def predict(self, word=None):
        current_node = self.root
        if word:
            for letter in word:
                if letter in current_node.children:
                    current_node = current_node.children[letter]
        def deep(node):
            if not node.children: return print(node.value)
            for key, value in node.children.items():
                deep(value)
        return deep(current_node)

    def traverse(self):
        def deep(node):
            if not node.children: return print(f': {node.value}')
            for key, value in node.children.items():
                print(f'-{key}',end='')
                deep(value)
        return deep(self.root)

    def search(self, key):
        current_node = self.root
        for letter in key:
            if letter not in current_node.children:
                raise ValueError(f'{key} not found')
            current_node = current_node.children[letter]
        return current_node.value
