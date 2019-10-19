""" 
Reverse a decent implemntation of a linked list
"""
# The decent implemetation
class linked_list():
    def __init__(self):
        self.head = None

    class node():
        def __init__(self, v=None):
            self.value = v
            self.next = None

    def append(self, v):
        if not self.head:
            self.head = self.node(v)
            return
        current_node = self.head
        while current_node.next:  # traverse
            current_node = current_node.next
        current_node.next = self.node(v)

    def traverse(self):
        def deep(x, i):
            if not x: return
            print(f'index: {i}, value:{x.value}')
            deep(x.next, i+1)
        return deep(self.head, 0)

    def reverse(self):
        def deep(parent, current_node):
            if not current_node:
                self.head = parent
                return
            sentinel = current_node.next
            current_node.next = parent
            deep(current_node, sentinel)
        return deep(None, self.head)

# test
print('testing with: (69) --> (117) --> (3) --> (4)')
foo = linked_list()
foo.append(69)
foo.append(117)
foo.append(3)
foo.append(4)
