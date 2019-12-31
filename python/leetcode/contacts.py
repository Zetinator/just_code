"""https://www.hackerrank.com/challenges/contacts/problem

We're going to make our own Contacts application! The application must perform two types of operations:

add name, where  is a string denoting a contact name. This must store  as a new contact in the application.
find partial, where  is a string denoting a partial name to search the application for. It must count the number of contacts starting with  and print the count on a new line.
Given  sequential add and find operations, perform each operation in order.
"""

class Trie():
    class Node():
        def __init__(self):
            self.data = None
            self.counter = 0
            self.children = {}
    def __init__(self):
        self.root = self.Node()
    def add(self, key):
        if not key: return
        current_node = self.root
        for letter in key:
            if letter not in current_node.children:
                current_node.children[letter] = self.Node()
            current_node.counter += 1
            current_node = current_node.children[letter]
        current_node.counter += 1
        current_node.data = key
    def find(self, key):
        if not key: return 0
        current_node = self.root
        for letter in key:
            if letter not in current_node.children: return 0
            current_node = current_node.children[letter]
        return current_node.counter

trie = Trie()
def contacts(queries):
    """interface to process the queries...
    """
    if q[0] == 'add': trie.add(q[1])
    else: print(trie.find(q[1]))

# read from stdin
trie = Trie()
for _ in range(int(input())):
    q = [e for e in input().split()]
    contacts(q)

# local test...
trie.add('s')
trie.add('ss')
trie.add('sss')
trie.add('ssss')
trie.add('sssss')
print(trie.find('s'))
print(trie.find('ss'))
print(trie.find('sss'))
print(trie.find('ssss'))
print(trie.find('sssss'))
print(trie.find('ssssss'))

