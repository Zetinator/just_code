"""implementation of the quick select algorithm
https://en.wikipedia.org/wiki/Quickselect
"""

def quick_select(x, k):
    """returns the element of k order in the list
    """
    pivot = x[0]
    minor = [e for e in x[1:] if e < pivot]
    mayor = [e for e in x[1:] if e > pivot]
    if k == len(minor): return pivot
    if k < len(minor):
        return quick_select(minor, k)
    else:
        return quick_select(mayor, k-len(minor+[pivot]))  # -pivot and -len(minor)
