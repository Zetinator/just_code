"""https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=stacks-queues

In this challenge, you must first implement a queue using two stacks. Then process  queries, where each query is one of the following  types:

1 x: Enqueue element  into the end of the queue.
2: Dequeue the element at the front of the queue.
3: Print the element at the front of the queue.
"""

class MyQueue(object):
    """implements a queue with 2 stacks
    naive approach enqueue expensive
    """
    def __init__(self):
        self.main_stack = []
        return

    def peek(self):
        return self.main_stack[-1]

    def pop(self):
        self.main_stack.pop()

    def put(self, value):
        aux_stack = []
        for e in range(len(self.main_stack)):
            aux_stack.append(self.main_stack.pop())
        self.main_stack.append(value)
        for e in range(len(aux_stack)):
            self.main_stack.append(aux_stack.pop())


class MyQueue(object):
    """implements a queue with 2 stacks
    naive approach, expensive dequeue
    """
    def __init__(self):
        self.main_stack = []
        self.pop_stack = []
        return

    def peek(self):
        # if empty flush the main_stack into the pop stack
        if not self.pop_stack:
            for e in range(len(self.main_stack)):
                self.pop_stack.append(self.main_stack.pop())
        return self.pop_stack[-1]

    def pop(self):
        # if empty flush the main_stack into the pop stack
        if not self.pop_stack:
            for e in range(len(self.main_stack)):
                self.pop_stack.append(self.main_stack.pop())
        self.pop_stack.pop()


    def put(self, value):
        self.main_stack.append(value)
