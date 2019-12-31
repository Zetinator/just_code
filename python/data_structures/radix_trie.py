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
        def r(node):
            if node.data != None: nodes.append(str(node.data))
            for k,child in node.children.items(): r(child)
        r(self.root)
        return '\n'.join(nodes)

    def insert(self, key):
        """insert a new key
        """
        data = key
        def lcp(key_1, key_2):
            """largest common prefix
            """
            for i in range(min(len(key_1),len(key_2))):
                if key_1[i] != key_2[i]: return i
            return i+1
        current_node = self.root
        print(f'-------------------------------------------------------------------')
        print(f'inserting key: {key}')
        while key:
            if not current_node.children:
                print(f'no children... inserting key {key}')
                current_node = current_node.children.setdefault(key, self.Node())
                break
            for k, child in current_node.children.items():
                # find common root...
                i = lcp(k, key)
                prefix, suffix, key = k[:i], k[i:], key[i:]
                print(f'prefix: {prefix}, suffix: {suffix}, key: {key}, at: {i}')
                if prefix and suffix:
                    # split...
                    current_node.children[prefix] = self.Node()
                    del(current_node.children[k])
                    # original branch...
                    current_node.children[prefix].children[suffix] = self.Node()
                    current_node.children[prefix].children[suffix].data = child.data
                    current_node.children[prefix].children[suffix].children = child.children
                    current_node = current_node.children[prefix]
                    break
                elif prefix and not suffix:
                    # keep moving forward...
                    current_node = child
                    break
            print(f'no common prefix in the children... inserting {key} anyways...')
            current_node = current_node.children.setdefault(key, self.Node())
            key = ''
        # create new branch...
        # current_node = current_node.children.setdefault(key, self.Node())
        current_node.data = data

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
keys = 'erick quiere a marion mariana quien es esa? achso marina no?'.split()
rt = RTrie(keys)
