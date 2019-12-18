"""https://www.hackerrank.com/challenges/maximum-subarray-sum/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=search

Complete the maximumSum function in the editor below. It should return a long integer that represents the maximum value of subarray_sum % modul
"""

def maximumSum(arr, m):
    """kadane's algorithm, but with a modulo there
    it doesnt work... kadane's algorithm expects the + operator
    to increase the previous value when adding positive numbers... 
    which doenst occur in modulo arithmetics
    """
    current_max = best = 0
    for e in arr:
        current_max = max([0] + [(current_max+e%m)%m] + [e%m])
        best = max(best, current_max)
    return best

from functools import lru_cache
def maximumSum(arr, m):
    """dynamic programming
    solved but crashes hackerrank with so many levels
    """
    arr = tuple(arr)

    @lru_cache(maxsize=None)
    def r(arr, m, c_arr):
        if not arr: return (sum(c_arr)%m, c_arr)
        print(f'arr: {arr}, c_arr: {c_arr}')
        return max(r(arr[1:], m, c_arr),
                    r(arr[1:], m, c_arr + (arr[0],)),
                    r(arr[1:], m, (arr[0],)))
    return r(arr, m, ())

from bisect import insort, bisect_right
def maximumSum(a, m):
    """solution of a random guy with a pseudo ordered array
    """
    # Create prefix tree
    prefix = [0] * len(a)
    curr = 0;
    for i in range(len(a)):
        curr = (a[i] % m + curr) % m
        prefix[i] = curr
    # Compute max modsum
    pq = [prefix[0]]
    maxmodsum = max(prefix)
    for i in range(1, len(a)):
        # Find cheapest prefix larger than prefix[i]
        left = bisect_right(pq, prefix[i])
        if left != len(pq):
            # Update maxmodsum if possible
            modsum = (prefix[i] - pq[left] + m) % m
            maxmodsum = max(maxmodsum, modsum)
        # add current prefix to heap
        insort(pq, prefix[i])
    return maxmodsum


def maximumSum(arr, m):
    """damn modular arithmetics...
    we find the max between the modules calculated in the prefix sum
    and the minimum "reset" of values in this prefix array made by the modulo operation
    so we find the minimum change in the sorted prefix_sum array
    we focus on those with the original indexes inverted in this new sorted array...
    https://www.quora.com/What-is-the-logic-used-in-the-HackerRank-Maximise-Sum-problem
    """
    # build prefix_sum
    prefix_sum = []
    sum_acc = 0
    for i,e in enumerate(arr):
        sum_acc = e + sum_acc
        prefix_sum.append((sum_acc%m, i))
    # sort
    prefix_sum.sort()
    minima = float('inf')
    for i in range(len(arr)-1):
        # find the min difference between consecutives with indexes inverted
        if prefix_sum[i][1] > prefix_sum[i+1][1]:
            delta = abs(prefix_sum[i][0] - prefix_sum[i+1][0])
            if delta < minima: minima = delta
    # we need to add the modulo to this minimum distance found... intuitive demonstration
    return max(m-minima, prefix_sum[-1][0])


arr = [3, 3, 9, 9, 5]
m = 7
# arr = [1,5,9]
# m = 5
# arr = [-2, -3, 4, -1, -2, 1, 5, -3]
# m = 5
print(f'testing with: {arr}')
print(f'ans: {maximumSum(arr, m)}')
