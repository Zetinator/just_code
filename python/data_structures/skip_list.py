"""custom implementation of a skip list with the purpose of practice
http://cglab.ca/~morin/teaching/5408/refs/p90b.pdf
https://en.wikipedia.org/wiki/Skip_list

the ADT contains the following methods:
    - insert: insert a new node in the tree
    - search: return the node with the given value
    - delete: delete the given value from the tree
    - successor: return the next in order successor
"""
from random import uniform

class SkipList():
    class Node():
        """Node basic chainable storage unit
        """
        def __init__(self, x=None):
            self.value = x
            self.next = None
            self.down = None
        def __repr__(self):
            return repr(self.value)

    def __init__(self, x=[]):
        self.head = self.Node(-float('inf'))
        for e in x:
            self.insert(e)

    def __repr__(self):
        res = []
        current_head = self.head
        level = 0
        while current_head:
            tmp = [f'{level}: ']
            node = current_head
            while node:
                tmp.append(f'({node})->')
                node = node.next
            res.append(''.join(tmp))
            current_head = current_head.down
            level += 1
        return '\n'.join(res)

    def insert(self, value):
        """insert a new node into the skip list
        note: promotions with p = .5
        """
        # skip search
        node, node_stack = self.head, []
        while node.down:
            # go right
            while node.next and node.next.value < value: node = node.next
            # go down... keep track of the jumps
            node_stack.append(node)
            node = node.down
        # standard linked list search
        while node.next and node.next.value < value: node = node.next
        # standard insertion...
        _, new_node = node.next, self.Node(value)
        node.next = new_node
        node.next.next = _
        # promote? flip a coin
        while uniform(0,1) < .5:
            if node_stack:
                # standard insertion, one level up
                node = node_stack.pop()
                _, node.next = node.next, self.Node(value)
                node.next.next, node.next.down = _, new_node
                new_node = node.next
            else:
                # promote to new level
                new_head = self.Node(-float('inf'))
                new_head.next = self.Node(value)
                new_head.next.down = new_node
                new_head.down, self.head = self.head, new_head
                return

    def delete(self, value):
        # search
        node, node_stack = self.head, []
        while node.down:
            # go right
            while node.next and node.next.value < value: node = node.next
            # erase possible instance
            if node.next and node.next.value == value:
                node.next = node.next.next
            # go down...
            node_stack = node
            node = node.down
        # standard linked list search
        while node.next and node.next.value < value:
            node = node.next
        # erase possible instance
        if node.next and node.next.value == value:
            node.next = node.next.next

    def successor(self, value):
        """search for a successor of a node with the given value
        """
        # skip search
        node = self.head
        while node.down:
            # go right
            while node.next and node.next.value <= value: node = node.next
            # go down...
            node = node.down
        # standard linked list search
        while node:
            if node.value == value: return node.next
            node = node.next
        raise ValueError(f'{value} not found')

    def search(self, value):
        """search for a node with the given value
        """
        # skip search
        node = self.head
        while node.down:
            # go right
            while node.next and node.next.value < value: node = node.next
            # go down...
            node = node.down
        # standard linked list search
        while node:
            if node.value == value: return node
            node = node.next
        raise ValueError(f'{value} not found')
