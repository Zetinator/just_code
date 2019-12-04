class min_heap():
    def __init__(self):
        self._ = []
    def get_parent(self, index):
        if index == 0: return 0
        return (index-1)//2
    def has_left(self, index):
        return index*2 + 1 < len(self._)
    def has_right(self, index):
        return index*2 + 2 < len(self._)
    def left(self, index):
        return index*2 + 1
    def right(self, index):
        return index*2 + 2
    def swap(self, i, j):
        self._[i], self._[j] = self._[j], self._[i]
        return
    def insert(self, x):
        i = len(self._)
        self._.append(x)
        while self._[self.get_parent(i)] > self._[i]:
            self.swap(self.get_parent(i), i)
            i = self.get_parent(i)
        return
    def pop(self):
        self._[0], self._[-1] = self._[-1], self._[0]  # swap first and last
        ans = self._.pop()
        i = 0
        # sift down
        while (self.has_left(i) and self._[self.left(i)] < self._[i]) or \
               (self.has_right(i) and self._[self.right(i)] < self._[i]):
            max_child = self.left(i)
            if self.has_right(i) and self._[self.left(i)] > self._[self.right(i)]:
                max_child = self.right(i)
            self.swap(i, max_child)
            i = max_child
        else:
            return ans


# test
test = [2,7,26,25,19,17,1,90,3,36]
print(f'testing with: {test}')
heap = min_heap()
for e in test:
    heap.insert(e)
print(f'heap created: {heap._}')
ans = []
for e in range(len(heap._)):
    ans.append(heap.pop())
print(f'heap_sort: {ans}')
