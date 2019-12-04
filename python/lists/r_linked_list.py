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
        def deep(v, parent, current_node):
            if not current_node:
                current_node = self.node(v)
                if parent:
                    parent.next = current_node
                else:
                    self.head = current_node
                return
            return deep(v, current_node, current_node.next)
        return deep(v, None, self.head)

    def traverse(self):
        def deep(x, i):
            if not x: return
            print(f'index: {i}, value:{x.value}')
            deep(x.next, i+1)
        return deep(self.head, 0)

    def search(self, wanted):
        def deep(wanted, current_node, i):
            if not current_node: raise KeyError(f'{wanted}: NOT FOUND')
            if current_node.value == wanted: return 
            return deep(wanted, current_node.next, i+1)
        return deep(wanted, self.head, 0)

    def insert(self, v, index):
        def deep(v, index, parent, current_node, current_index):
            if not current_node:
                current_node = self.node(v)
                if not parent:  # no parent? must be root
                    self.head = current_node
                    return
                parent.next = current_node
                return
            if current_index == index:
                parent.next = self.node(v)
                parent.next.next = current_node
                return
            return deep(v, index, current_node, current_node.next, current_index+1)
        return deep(v, index, None, self.head, 0)

    def remove(self, v):
        def deep(v, parent, current_node):
            if not current_node: raise KeyError('{v}: NOT FOUND')
            if current_node.value == v:
                if not parent:  # no parent? must be root
                    self.head = None
                    return
                parent.next = current_node.next
                return
            return deep(v, current_node, current_node.next)
        return deep(v, None, self.head)

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

