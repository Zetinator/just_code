"""https://www.hackerrank.com/challenges/largest-rectangle/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=stacks-queues

Complete the function largestRectangle int the editor below. It should return an integer representing the largest rectangle that can be formed within the bounds of consecutive buildings.

largestRectangle has the following parameter(s):

h: an array of integers representing building heights
"""
from functools import lru_cache
import sys
sys.setrecursionlimit(100000)

def largestRectangle(h):
    """dynamic programming
    almost... I got the time limit exception
    """
    @lru_cache(maxsize=None)
    def r(i, current_min):
        n, _from = current_min
        # base case
        if i == len(h): return n*(i+1-_from)
        # the current min is not valid anymore return
        # or... inheritate the path of the old one
        if h[i] <= n: return max(n*(i+1-_from), r(i+1, (h[i], _from)))
        # guess, wheter we take it or not
        return max(r(i+1, current_min),  # dont take it
                    r(i+1, (h[i], i+1)))  # take it
    return r(1, (h[0], 1))

def largestRectangle(h):
    """stack
    """
    stack = []
    current_max = -float('inf')
    h.append(0)
    for i in range(len(h)):
        left_index = i
        while stack and h[i] < stack[-1][0]:
            n, left_index = stack.pop()
            # current max vs inheritance vs the kindom of the last one ends here
            current_max = max([current_max] + [h[i]*(i+1 -left_index)] + [n*(i-left_index)])
        stack.append((h[i], left_index))
    return current_max

# test
test = [1,2,3,4,5]
test = [1,3,5,9,11]
test = [11,11,10,10,10]
print(f'testing with: {test}')
print(f'ans: {largestRectangle(test)}')
