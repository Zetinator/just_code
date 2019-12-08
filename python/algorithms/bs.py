"""implementation of the binary search algorithm
https://en.wikipedia.org/wiki/Binary_search_algorithm
"""

def bs(x: list, val) -> int:
    """orders in-place the given list
    the elements in the list must support the '<' comparison operator
    """
    if not x or not val: ValueError(f'{val} not in the list')
    l, r = 0, len(x)
    while l < r:
        m = (l+r)//2
        if x[m] == val: return m
        if val < x[m]:
            r = m
        else:
            l = m+1
    raise ValueError(f'{val} not in the list')
