"""custom implementation of a self heap tree with the purpose of practice
the ADT contains the following methods:
    - push
    - peek
    - pop
"""
from data_structures import max_heap

class Heap(max_heap.Heap):

    def push(self, x):
        """push a new element into the heap
        """
        return super().push(-x)

    def peek(self):
        """peek the maximum
        """
        return -super().peek()

    def pop(self):
        """pop the maximum
        """
        return -super().pop()

    def __len__(self):
        return len(self._)

    def __repr__(self):
        aux = [-e for e in self._]
        return str(aux)

