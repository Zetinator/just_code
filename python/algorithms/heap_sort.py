"""implementation of the heap sort algorithm O(Nlog(N))
heapify functional aproach, with creation in O(N)

https://en.wikipedia.org/wiki/Heapsort
"""
def sift_d(x, i):
    i_left = lambda: i*2 + 1
    i_right = lambda: i*2 + 2
    while (i_left() < len(x) and x[i_left()] > x[i]) or \
          (i_right() < len(x) and x[i_right()] > x[i]):
        max_child = i_left()
        if i_right() < len(x) and x[i_right()] > x[i_left()]:
            max_child = i_right()
        x[i], x[max_child] = x[max_child], x[i]  # swap
        i = max_child
    return x

def heapify(x: []) -> []:
    for index in reversed(range(0, len(x)//2)):
        sift_d(x, index)
    return x

def heap_sort(x):
    heapify(x)
    for i in range(1, len(x)):
        x[-i], x[0] = x[0], x[-i]
        x[:-i] = sift_d(x[:-i], 0)
    return x
