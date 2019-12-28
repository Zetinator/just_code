"""https://www.hackerrank.com/challenges/ctci-fibonacci-numbers/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=recursion-backtracking

The Fibonacci Sequence

The Fibonacci sequence appears in nature all around us, in the arrangement of seeds in a sunflower and the spiral of a nautilus for example.

The Fibonacci sequence begins with  and  as its first and second terms. After these first two elements, each subsequent element is equal to the sum of the previous two elements.
"""

from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibonacci(n-1) + fibonacci(n-2)

test = 6
print(f'ans: {fibonacci(test)}')
