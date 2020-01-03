"""custom implementation of a min heap tree with the purpose of practice
the ADT contains the following methods:
    - push
    - peek
    - pop
"""
class Heap():
    def __init__(self, x=[]):
        self.v = []
        for e in x:
            self.push(e)

    def __len__(self):
        return len(self.v)

    def __repr__(self):
        return str(self.v)

    def push(self, x):
        """push a new element into the heap
        can also push tuples with the priority as the first element :)
        """
        # special case: push None element
        if not x: return
        # auxiliar function to compute the parent index
        parent = lambda i: max((i-1)//2, 0)
        v = self.v  # alias because i am lazy to write
        # special case: empty heap
        if not v: v.append(x); return
        # general case
        i = len(v)
        v.append(x)
        # bubble up...
        while v[parent(i)] > v[i]:  # heapify-up
            v[parent(i)], v[i] = v[i], v[parent(i)]
            i = parent(i)

    def peek(self):
        """peek the minimum
        """
        # special case: empty heap
        if not self.v: return
        return self.v[0]

    def pop(self):
        """pop the minimum
        """
        v = self.v  # alias again
        # special case: empty heap
        if not v: return
        # swap max <-> last
        v[0], v[-1] = v[-1], v[0]
        minimum = v.pop()
        # bubble down
        i = 0
        left = lambda: i*2 + 1 if i*2 + 1 < len(v) else False
        right = lambda: i*2 + 2 if i*2 + 2 < len(v) else False
        while left() and v[left()] < v[i] or right() and v[right()] < v[i]:
            max_child = left()
            if right() and v[right()] < v[left()]:
                max_child = right()
            v[i], v[max_child] = v[max_child], v[i]  # swap
            i = max_child
        return minimum
