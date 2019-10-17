""" 
Reverse a decent implemntation of a linked list
"""
# The decent implemetation
class linked_list():
    def __init__(self):
        self.head = self.node()
    class node():
        def __init__(self, v=None):
            self.value = v
            self.next = None

    def append(self, v):
        if self.head.value == None:
            self.head.value = v
            return
        current_node = self.head
        while current_node.next:  # traverse
            current_node = current_node.next
        current_node.next = self.node(v)
    def traverse(self):
        if self.head.value == None: return
        if not self.head.next: return print(f'STATUS: index:0, value:{self.head.value}')
        current_node = self.head
        index = 0
        while current_node.next:
            print(f'STATUS: index:{index}, value:{current_node.value}')
            index += 1
            current_node = current_node.next
        return
    def reverse(self):
        # aux pointers
        before = None
        current = None
        after = None
        # do nothing cases
        if self.head.value == None: return
        if self.head.next == None: return
        # just 2 nodes 
        if self.head.next.next == None:
            tmp_node = self.head
            self.head = self.head.next
            self.head = tmp_node
            return
        


# test
print('testing with: (1) --> (2) --> (3) --> (4)')
foo = linked_list()
foo.append(1)
foo.append(2)
# foo.append(3)
# foo.append(4)
# foo.append(5)
