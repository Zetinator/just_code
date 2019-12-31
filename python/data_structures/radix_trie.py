"""custom implementation of a radix trie with the purpose of practice
the ADT contains the following methods:
    - insert
    - search
    - delete
"""
class RTrie():
    class Node():
        """Node basic chainable storage unit
        """
        def __init__(self, x=None):
            self.data = x
            self.children = {}

    def __init__(self, keys=None):
        self.root = self.Node()
        if keys:
            for key in keys:
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
        """insert a new key... recursive attempt
        """
        data = key
        def lcp(key_1, key_2):
            """largest common prefix
            """
            for i in range(min(len(key_1),len(key_2))):
                if key_1[i] != key_2[i]: return i
            return i+1
        def r(current_node, key):
            """recursive branching...
            no children -> new branch
            common root + remainings -> split and extend
            common root + no remainings -> extend
            no comomon root -> create new branch
            """
            # base case... no children
            if not current_node.children:
                current_node.children.setdefault(key, self.Node()).data = data
                return
            # look for similar roots in the children...
            for k, child in current_node.children.items():
                i = lcp(k, key)
                prefix, suffix, key = k[:i], k[i:], key[i:]
                if prefix and suffix:
                    # common root found... branching
                    current_node.children[prefix] = self.Node()
                    del(current_node.children[k])
                    # append suffixs to common root
                    current_node.children[prefix].children[suffix] = self.Node()
                    current_node.children[prefix].children[suffix].data = child.data
                    current_node.children[prefix].children[suffix].children = child.children
                    # recurse on the shared root
                    return r(current_node.children[prefix], key)
                elif prefix and not suffix:
                    # common root found... extending
                    return r(child, key)
            # no common root... create new child branch
            current_node.children.setdefault(key, self.Node()).data = data
        return r(self.root, key)

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

keys = 'erick quiere mucho a su marion aunque ella ya no nos quiera...'.split()
rt = RTrie(keys)
