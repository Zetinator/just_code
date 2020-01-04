"""https://www.hackerrank.com/challenges/jim-and-the-skyscrapers/problem+

Jim has invented a new flying object called HZ42. HZ42 is like a broom and can only fly horizontally, independent of the environment. One day, Jim started his flight from Dubai's highest skyscraper, traveled some distance and landed on another skyscraper of same height! So much fun! But unfortunately, new skyscrapers have been built recently.
"""
from math import factorial
def permutations(n, r=2):
    """permutations of n in r
    """
    if n < r: return 0
    return factorial(n)//factorial(n-r)

from collections import Counter
def solve(arr):
    """stack + counter solution
    """
    stack, counter = [], Counter()
    res = 0
    # we add a dummy "stack popper" at the end of arr
    for i,e in enumerate(arr + [float('inf')]):
        # pop all the smaller buildings from the stack
        while stack and e > stack[-1]:
            adios = stack.pop()
            res += permutations(counter[adios])
            del(counter[adios])
        # add the building to our stack
        if not stack or e < stack[-1]:
            stack.append(e)
            counter[e] += 0
        # if is already in the stack increase counter...
        if e in counter: counter[e] += 1
    return res

# local test
# test = """3 2 1 2 3 3"""
# test = [int(e) for e in test.split()]

with open('./test_data.txt', 'r') as f:
    for line in f:
        test = [int(n) for n in line.split()]
print(f'testing with: {test[:10]}...')
print(f'ans: {solve(test)}')
