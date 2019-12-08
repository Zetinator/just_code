"""implementation of the bubble sort algorithm
https://en.wikipedia.org/wiki/Bubble_sort
"""

def bubble_sort(x: list) -> list:
    """orders in-place the given list
    the elements in the list must support the '<' comparison operator
    """
    # special case: empty list
    if not x: return
    # general case
    l, r = 0, len(x)-1
    swap = True
    while swap:
        swap = False
        l = 0
        while l < r:
            if not x[l] < x[l+1]:
                swap = True
                x[l], x[l+1] = x[l+1], x[l]
            l += 1
        r -= 1
    return x
