"""implementation of the quick select algorithm
https://en.wikipedia.org/wiki/Quickselect
"""

# def quick_select(x, k):
    # """returns the element of k order in the list
    # """
    # pivot = x[0]
    # minor = [e for e in x[1:] if e < pivot]
    # mayor = [e for e in x[1:] if e > pivot]
    # if k == len(minor): return pivot
    # if k < len(minor):
        # return quick_select(minor, k)
    # else:
        # return quick_select(mayor, k-len(minor+[pivot]))  # -pivot and -len(minor)

from random import uniform
def quick_select(x: list, k: int) -> int:
    """random version, it's been a long time old friend...
    NOTE: k -> (1, len(x))
    """
    pivot = int(uniform(0, len(x)))
    left, right = [], []
    for i, e in enumerate(x):
        if e <= x[pivot] and i != pivot: left.append(e)
        if e > x[pivot]: right.append(e)
    if k == len(left): return x[pivot]
    if k < len(left):
        return quick_select(left, k)
    else:
        return quick_select(right, k-len(left)-1)
