"""https://www.hackerrank.com/challenges/maximum-xor/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=miscellaneous

You are given an array  of  elements. A list of integers,  is given as an input, find the maximum value of xor(q, arr[i]) for all elements, where xor() represents xor of two elements.
"""
class Trie():
    """bitwise trie implementation
    basically a normal bst, but with a dictionary
    """
    class Node():
        def __init__(self):
            self.data = None
            self.children = {}

    def __init__(self, x=[]):
        """can be initialized from an array of keys
        """
        self.root = self.Node()
        for key in x:
            self.insert(key)

    def __repr__(self):
        nodes = []
        def r(node):
            if node.data: nodes.append(str(node.data))
            for k,child in node.children.items(): r(child)
        r(self.root)
        return '\n'.join(nodes)

    def predict(self, key=None):
        if not key or not self.root.children: return []
        res = []
        current_node = self.root
        for letter in key:
            if letter in current_node.children:
                current_node = current_node.children[letter]
        def deep(node):
            if node.data != None: return res.append(node.data)
            for key, data in node.children.items(): deep(data)
        deep(current_node)
        return res

    def insert(self, key, data):
        if key == None: return
        current_node = self.root
        for bit in key:
            if bit not in current_node.children:
                current_node.children[bit] = self.Node()
            current_node = current_node.children[bit]
        current_node.data = data

    def search_max(self, key, n):
        if key == None: return
        return max([n^pred for pred in self.predict(key)])

def maxXor(arr, queries):
    """return the max xor of the array with the query
    """
    maximum = len(bin(max(arr)))-2
    get_binkey = lambda key: bin(key)[2:].zfill(maximum)
    xor = lambda n: ''.join([str(int(not int(i))) for i in bin(n)[2:].zfill(maximum)])
    t = Trie()
    for n in arr:
        print(f'inserting: {(get_binkey(n), n)}')
        t.insert(get_binkey(n), n)
    res = []
    for q in queries:
        print(f'look for {q} in xor: {xor(q)}')
        res.append(t.search_max(xor(q), q))
    return res

def maxXor(arr, queries):
    trie_root = {}
    # we need to pad the binary representation with zeros
    k = len(bin(max(arr+queries))) - 2
    for number in ['{:b}'.format(x).zfill(k) for x in arr]:
        current_node = trie_root
        for bit in number:
            current_node = current_node.setdefault(bit, {})
    ans = []
    for n in queries:
        current_node = trie_root
        s = []
        for bit in'{:b}'.format(n).zfill(k) :
            # toggle bit
            toggled = str(int(bit)^1)
            # use trie or keep this one...
            toggled = toggled if toggled in current_node else bit
            s += [toggled]
            # move forward in the tree
            current_node = current_node[toggled]
        # back to int and then xor
        ans.append(int(''.join(s), 2) ^ n)
    return ans

test = """5 1 7 4 3"""
test = """1 0 2"""
test = """1 3 5 7"""
test = [int(n) for n in test.split()]
queries = [2, 0]
queries = [3, 7, 2]
queries = [17, 6]
print(f'testing with: arr: {test}, queries: {queries}')
print(f'ans: {maxXor(test, queries)}')
t = Trie()
