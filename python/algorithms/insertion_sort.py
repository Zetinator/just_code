"""implementation of the insertion sort algorithm
https://en.wikipedia.org/wiki/Selection_sort
"""
def insertion_sort(x: list) -> list:
    """returns
    returns the index of the given element val in the list
    """
    if not x: return
    for i in range(1, len(x)):
        while i > 0 and x[i-1] > x[i]:
            x[i], x[i-1] = x[i-1], x[i]  # the n^2 complexity is here...
            i -= 1
    return x
