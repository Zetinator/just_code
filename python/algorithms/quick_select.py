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
    if not x: return
    if len(x) == 1: return x[0]
    # choose a random pivot
    pivot = int(uniform(0, len(x)))
    # divide
    left = [e for e in x if e <= x[pivot]]
    right = [e for e in x if e > x[pivot]]
    # keep exploring the DAG
    if len(left) > k:
        return quick_select(left, k)
    else: 
        return quick_select(right, k-len(left))
