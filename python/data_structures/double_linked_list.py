"""custom implementation of a double linked list with the purpose of practice
the ADT contains the following methods:
    - append
    - insert
    - search
    - delete
    - traverse
"""
class DoubleLinkedList():
    class Node():
        """Node basic chainable storage unit
        """
        def __init__(self, x=None, prev=None):
            self.value = x
            self.prev = prev
            self.next = None

    def __init__(self, x=None):
        self.head = None
        if x:
            for e in x:
                self.append(e)

    def append(self, x):
        """append a new node to the tail
        """
        if not self.head:
            self.head = self.Node(x)
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = self.Node(x, prev=current_node)
        return

    def search(self, x):
        """search for a node with the given 'x' value
        """
        current_node = self.head
        while current_node:
            if current_node.value == x: return current_node
            current_node = current_node.next
        raise ValueError(f'{x} not found')

    def insert(self, x, index):
        """inserts a new node with value 'x' at the 'index' position
        """
        # special case: empty list
        if not self.head:
            self.append(x)
            return
        # special case: replace head
        if index == 0:
            tmp = self.head
            self.head = self.Node(x)
            self.head.next = tmp
            return
        # general case
        current_node = self.head
        while current_node.next and (index-1):
            current_node = current_node.next
            index -= 1
        tmp = current_node.next
        current_node.next = self.Node(x, prev=current_node)
        current_node.next.next = tmp
        
    def delete(self, x):
        """deletes the node with value 'x'
        """
        # special case: empty list
        if not self.head: raise ValueError(f'{x} not in the list')
        # special case: delete head
        if self.head.value == x:
            self.head = self.head.next
            return
        # general case
        current_node = self.head
        while current_node.next:
            if current_node.next.value == x:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
        raise ValueError(f'{x} not in the list')

    def traverse(self):
        """print all the nodes in the link
        """
        current_node = self.head
        while current_node:
            print(f'{current_node.value}', end=' -> ')
            current_node = current_node.next
        print('null')

    def __repr__(self):
        current_node = self.head
        ans = []
        while current_node:
            ans.append(f'{current_node.value} -> ')
            current_node = current_node.next
        ans.append('null')
        return ''.join(ans)
