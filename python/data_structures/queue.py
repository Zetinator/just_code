"""custom implementation of a queue with the purpose of practice
the ADT contains the following methods:
    - push
    - pop
    - peek
"""
class Queue():
    class Node():
        """Node basic chainable storage unit
        """
        def __init__(self, x=None, prev=None):
            self.value = x
            self.prev = prev
            self.next = None

    def __init__(self, x=None):
        self.tail = None
        self.head = self.tail
        if x:
            for e in x:
                self.push(e)

    def push(self, x):
        """push a new node into the queue
        """
        # special case: empty queue
        if not self.head:
            self.head = self.Node(x)
            self.tail = self.head
            return
        # general case
        tmp = self.head
        self.head = self.Node(x)
        self.head.next = tmp
        self.head.next.prev = self.head
        return

    def peek(self):
        """peek the top node of the queue
        """
        return self.tail

    def pop(self):
        """pop the top node of the queue
        """
        # special case: empty list
        if not self.tail: return
        # general case
        tmp = self.tail
        self.tail = self.tail.prev
        return tmp
# test
test = Queue(range(10))
