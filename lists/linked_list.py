class node():
    def __init__(self, v=None):
        self.v = v
        self.next = None

class linked_list():
    def __init__(self):
        self.head = node()

    def append(self, v):
        if self.head.v == None:
            self.head.v = v
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = node(v)
    def prepend(self, v):
        if self.head.v == None:
            self.head.v = v
        else:
            current_node = node(v)
            current_node.next = self.head
            self.head = current_node
    def search(self, v):
        if self.head.v == None: return -1
        current_node = self.head
        index = 0
        while current_node.next:
            if current_node.v == v: return index
            current_node = current_node.next
            index += 1
        return -1
    def insert(self, v, index):
        if index == 0: return self.prepend(v)
        current_node = self.head
        while index:
            index -= 1
            vision_node = current_node.next.next
            if not vision_node: return -1
            current_node.next = node(v)
            current_node.next.next = vision_node
            return 0
        return -1
    def remove(self, v):
        if self.head.v == None: return -1
        if self.head.v == v:
            self.head = self.head.next
            return 0
        current_node = self.head
        while current_node.next:
            if current_node.next.v == v: 
                current_node.next = current_node.next.next
                return 0
            current_node = current_node.next
        return -1


# test
print('testing with: (1) --> (2) --> (3) --> (4)')
foo = linked_list()
foo.append(1)
foo.append(2)
foo.append(3)
foo.append(4)
foo.append(5)
