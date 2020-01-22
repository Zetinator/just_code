"""implementation of the merge sort algorithm
https://en.wikipedia.org/wiki/Merge_sort
"""

def merge_sort(x: list) -> list:
    """orders the given list
    the elements in the list must support the '<' comparison operator
    """
    # base case
    if len(x) == 1: return x
    # divide
    m = len(x)//2
    left = merge_sort(x[:m])
    right = merge_sort(x[m:])
    # conquer
    ans = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            ans.append(left[i])
            i += 1
        else:
            ans.append(right[j])
            j += 1
    ans += left[i:] + right[j:]
    return ans
