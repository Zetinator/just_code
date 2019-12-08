"""implementation of the quick sort algorithm
https://en.wikipedia.org/wiki/Quicksort
"""

def quick_sort(x: list) -> list:
    """orders the given list
    the elements in the list must support the '<' comparison operator
    """
    if not len(x): return x
    pivot = x[0]
    minor = quick_sort([e for e in x[1:] if e < pivot])
    mayor = quick_sort([e for e in x[1:] if e >= pivot])
    return minor + [pivot] + mayor
