"""https://www.hackerrank.com/challenges/bigger-is-greater/problem

Lexicographical order is often known as alphabetical order when dealing with strings. A string is greater than another string if it comes later in a lexicographically sorted list.
"""

from random import uniform
class Treap():
    class Node():
        def __init__(self, value):
            self.value = value
            self.priority = uniform(0,1)
            self.left = None
            self.right = None
    def __init__(self, v):
        self.root = None
        for e in v: self.insert(e)
    def rotate_right(self, node):
        tmp = self.Node(node.value)
        tmp.priority = node.priority
        tmp.left, tmp.right = node.left.right, node.right.right
        node.value = node.left.value
        node.priority = node.left.priority
        node.left, node.right = node.left.left, tmp
    def rotate_left(self, node):
        tmp = self.Node(node.value)
        tmp.priority = node.priority
        tmp.left, tmp.right = node.left.left, node.right.left
        node.value = node.right.value
        node.priority = node.right.priority
        node.left, node.right = tmp, node.right.right
    def insert(self, value):
        if not self.root: self.root = self.Node(value); return
        def r(node):
            # standard bst insertion
            if node.value == value: return
            if value < node.value:
                if node.left: return r(node.left, value)
                else: node.left = self.Node(value)
            else:
                if node.right: return r(node.right, value)
                else: node.right = self.Node(value)
            # repair tree...
            if value < node.value:
                if node.left.priority > node.priority: rotate_right(node)
            else:
                if node.right.priority > node.priority: rotate_left(node)

def biggerIsGreater(w):
    w = list(w)
    # check is sorted...
    if sorted(w, reverse=True) == w: return 'no answer'
    for k in reversed(range(len(w[:-1]))):
        if w[k] < w[k+1]: break
    # get successor
    stack = []
    for i in range(k+1, len(w)):
        while stack and w[i] > w[k] and w[i] <= stack[-1][0]:
            stack.pop()
        if not stack and w[i] > w[k]:
            stack.append((w[i], i))
    # swap...
    w[k], w[stack[-1][1]] = w[stack[-1][1]], w[k]
    # reverse...
    return ''.join(w[:k+1]) + ''.join(reversed(w[k+1:]))

test = "lmno"
test = "fedcbabcd"
res = biggerIsGreater(test)
