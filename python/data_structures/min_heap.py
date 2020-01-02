"""custom implementation of a min heap tree with the purpose of practice
the ADT contains the following methods:
    - push
    - peek
    - pop
"""
class Heap():
    def __init__(self, x=[]):
        self._ = []
        for e in x:
            self.push(e)

    def push(self, x):
        """push a new element into the heap
        can also push tuples with the priority as the first element :)
        """
        # special case: push None element
        if not x: return
        # auxiliar function to compute the parent index
        parent = lambda i: max((i-1)//2, 0)
        _ = self._  # alias because i am lazy to write
        # special case: empty heap
        if not _: _.append(x); return
        # general case
        i = len(_)
        _.append(x)
        while _[parent(i)] > _[i]:  # heapify-up
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
        minimum = _.pop()
        # sift down
        i = 0
        i_left = lambda: i*2 + 1
        i_right = lambda: i*2 + 2
        while (i_left() < len(_) and _[i_left()] < _[i]) or \
              (i_right() < len(_) and _[i_right()] < _[i]):
            max_child = i_left()
            if i_right() < len(_) and _[i_right()] < _[i_left()]:
                max_child = i_right()
            _[i], _[max_child] = _[max_child], _[i]  # swap
            i = max_child
        return minimum

    def __len__(self):
        return len(self._)

    def __repr__(self):
        return str(self._)
