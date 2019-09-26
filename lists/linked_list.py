class node():
    def __init__(self, v=None):
        self.v = v
        self.next = None

class linked_list():
    def __init__(self):
        self.tail = node()
        self.head = self.tail
    def insert(self, v):
        if self.tail.v == None:
            self.tail.v = v
        elif self.head.next == None:
            self.tail = node(v)
            self.head.next = self.tail
        else:
            self.tail.next = node(v)
            self.tail = self.tail.next

