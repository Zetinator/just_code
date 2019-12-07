class heap():
    def __init__(self):
        self._ = []

    def _sift_d(self, x, i):
        i_left = lambda: i*2 + 1
        i_right = lambda: i*2 + 2
        while (i_left() < len(x) and x[i_left()] > x[i]) or \
              (i_right() < len(x) and x[i_right()] > x[i]):
            max_child = i_left()
            if i_right() < len(x) and x[i_right()] > x[i_left()]:
                max_child = i_right()
            x[i], x[max_child] = x[max_child], x[i]  # swap
            i = max_child

    def insert(self, v):
        i = len(self._)
        self._.append(v)
        i_parent = lambda: (i-1)//2 * ((i-1)//2 > 0)
        while self._[i_parent()] < self._[i]:
            self._[i], self._[i_parent()] = self._[i_parent()], self._[i]  # swap
            i = i_parent()
    def pop(self, i=0):
        self._[0], self._[-1] = self._[-1], self._[0]  # swap
        ans = self._.pop()
        self._sift_d(self._, 0)
        return ans
              
class r_median():
    def __init__(self):
        self.min_heap = heap()
        self.max_heap = heap()
        self.median = None

    def insert(self, v):
        if not self.min_heap._:  # base case
            self.min_heap.insert(-v)
        elif v < -self.min_heap._[0]:
            self.max_heap.insert(v)
        else:
            self.min_heap.insert(-v)
        self.rebalance()

    def rebalance(self):
        if len(self.min_heap._) - len(self.max_heap._) > 1:
            self.max_heap.insert(-self.min_heap.pop())
        if len(self.max_heap._) - len(self.min_heap._) > 1:
            self.min_heap.insert(-self.max_heap.pop())
        if (len(self.min_heap._) + len(self.max_heap._)) % 2 == 0:
            self.median = (-self.min_heap._[0] + self.max_heap._[0])/2
        else:
            self.median = -self.min_heap._[0]
        print(f'min:{self.min_heap._}, max:{self.max_heap._}, median:{self.median}')

test = [3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]
print(f'testing with: {test}')
foo = r_median()
for e in test: foo.insert(e)
