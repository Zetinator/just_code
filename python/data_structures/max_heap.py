"""custom implementation of a self heap tree with the purpose of practice
the ADT contains the following methods:
    - push
    - peek
    - pop
"""
class Heap():

    def __init__(self, x=None):
        self._ = []
        if x:
            for e in x:
                self.push(e)

    def push(self, x):
        """push a new element into the heap
        """
        # auxiliar function to compute the parent index
        parent = lambda i: max((i-1)//2, 0)
        _ = self._  # alias because i am lazy to write
        # special case: empty heap
        if not _: _.append(x); return
        # general case
        i = len(_)
        _.append(x)
        while _[parent(i)] < _[i]:  # heapify-up
            # print(f'index: {i}, parent: {_[parent(i)]}, current: {_[i]}')
            _[parent(i)], _[i] = _[i], _[parent(i)]
            i = parent(i)

    def peek(self):
        """peek the maximum
        """
        # special case: empty heap
        if not self._: return
        return self._[0]

    def pop(self):
        """pop the maximum
        """
        _ = self._  # alias again
        # special case: empty heap
        if not _: return
        # swap max <-> last
        _[0], _[-1] = _[-1], _[0]
        maximum = _.pop()
        left = lambda i: i<<1 + 1
        right = lambda i: i<<1 + 2
        i = 0
        while (left(i) < len(_) and _[left(i)] > _[i]) or \
               (right(i) < len(_) and _[right(i)] > _[i]):
            max_child = left(i)
            if right(i) < len(_) and _[left(i)] < _[right(i)]:
                max_child = right(i)
            _[i], _[max_child] = _[max_child], _[i]
            i = max_child
        return maximum

# test
test = Heap([33, 66, 1, 65, 5, 7, 41, 74, 11, 45, 14, 60, 48, 84, 85, 31, 93, 63])
print(f'input: [33, 66, 1, 65, 5, 7, 41, 74, 11, 45, 14, 60, 48, 84, 85, 31, 93, 63]')
print(f'heap: {test._}')
