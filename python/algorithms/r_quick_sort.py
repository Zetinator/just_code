"""implementation of the quick sort algorithm with a random pivot
this implementation avoids the worst case scenario of n^2 complexity when
the input is already sorted

https://en.wikipedia.org/wiki/Quicksort#Choice_of_pivot
"""
from random import uniform

def r_quick_sort(x: list) -> list:
    """orders the given list
    the elements in the list must support the '<' comparison operator
    """
    # base case
    if len(x) < 2: return x
    # divide
    pivot = int(uniform(0, len(x)))
    minor, mayor = [], []
    for i,e in enumerate(x):
        if i == pivot: continue
        if e < x[pivot]:
            minor.append(e)
        else:
            mayor.append(e)
    minor = r_quick_sort(minor)
    mayor = r_quick_sort(mayor)
    # conquer
    return minor + [x[pivot]] + mayor
