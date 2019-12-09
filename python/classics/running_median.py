"""The median of a set of integers is the midpoint value of the data set for which an equal number of integers are less than and greater than the value. To find the median, you must first sort your set of integers in non-decreasing order, then:

https://www.hackerrank.com/challenges/find-the-running-median/problem
"""
from data_structures import max_heap


class RMedian():
    """class able to keep the running median on online insertions
    """
    def __init__(self):
        self.min_heap = max_heap.Heap()
        self.max_heap = max_heap.Heap()
        self.median = None

    def push(self, v):
        # special case: min heap empyty
        if not self.min_heap._:
            self.min_heap.push(-v)
            return
        if v < -self.min_heap.peek():
            self.max_heap.push(v)
        else:
            self.min_heap.push(-v)
        self.rebalance()

    def rebalance(self):
        # rebalance depending on who is bigger
        if len(self.min_heap) - len(self.max_heap) > 1:
            self.max_heap.push(-self.min_heap.pop())
        if len(self.max_heap._) - len(self.min_heap._) > 1:
            self.min_heap.push(-self.max_heap.pop())
        # compute current median
        if (len(self.min_heap) + len(self.max_heap)) % 2 == 0:
            self.median = (-self.min_heap.peek() + self.max_heap.peek())/2
        else:
            self.median = -self.min_heap.peek()
        # print(f'min:{self.min_heap}, max:{self.max_heap}, median:{self.median}')

test = [3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]
print(f'testing with: {test}')
foo = RMedian()
for e in test: foo.push(e)
