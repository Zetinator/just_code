"""implementation of the selection sort algorithm
https://en.wikipedia.org/wiki/Selection_sort
"""
def selection_sort(x: list) -> list:
    """returns
    returns the index of the given element val in the list
    """
    if not x: return
    for current in range(len(x)-1):
        minima = current
        for i in range(current, len(x)):  # someone said n^2?
            if x[i] < x[minima]:
                minima = i
        # swap
        x[current], x[minima] = x[minima], x[current]
    return x
