"""https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=recursion-backtracking

Davis has a number of staircases in his house and he likes to climb each staircase , , or  steps at a time. Being a very precocious child, he wonders how many ways there are to reach the top of the staircase.
"""

from functools import lru_cache

def stepPerms(n):
    """the classics...
    """
    # base cases...
    steps = {1:1, 2:2, 3:4}

    @lru_cache(maxsize=None)
    def r(n):
        # base case...
        if n <= 0: return 0
        if n in steps: return steps[n]
        return sum(r(n-step) for step in steps)
    return r(n)

# test
test = 7
print(f'ways in {test} stairs: {stepPerms(test)}')

