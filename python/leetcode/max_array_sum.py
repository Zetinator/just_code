"""https://www.hackerrank.com/challenges/max-array-sum/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=dynamic-programming

Given an array of integers, find the subset of non-adjacent elements with the maximum sum. Calculate the sum of that subset.

For example, given an array [-2,1,3,-4,5]  we have the following possible subsets:
"""
from functools import lru_cache
import sys
sys.setrecursionlimit(100000)

def maxSubsetSum(arr):
    """correct but crashes hackerrank with the depth of search
    """
    arr = tuple(arr)
    
    @lru_cache(maxsize=None)
    def r(arr, current_max):
        if not arr: return current_max
        # print(f'arr: {arr}, current_max: {current_max}')
        return max(r(arr[2:], current_max+arr[0]),  # we take it and we skip 1
                    r(arr[1:], current_max))  # or we don't
    return r(arr, 0)


def maxSubsetSum(arr):
    """bottom-up solution
    """
    # special case: short arr
    if len(arr) < 3: return max(arr)
    # general case
    memo = []
    # precompute the 2 base cases:
    memo.append(arr[0])
    memo.append(max(arr[:2]))
    current_max = -float('inf')
    for e in arr[2:]:
        memo.append(max([memo[-2] + e] + [memo[-1]] + [e]))
        current_max = max(current_max, memo[-1])
    return current_max

test = [2,1,5,8,4]
# test = [3, 5, -7, 8, 10]
print(f'testing with: {test}')
print(f'ans: {maxSubsetSum(test)}')
