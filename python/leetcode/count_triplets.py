"""
https://www.hackerrank.com/challenges/count-triplets-1/forum?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
You are given an array and you need to find number of tripets of indices  such that the elements at those indices are in geometric progression for a given common ratio  and .
"""
from functools import lru_cache
from collections import Counter

@lru_cache(maxsize=100)
def is_power(x, n, p=0):
    if x == 1: return p
    if x < 1: return -1
    return is_power(x/n, n, p+1)

@lru_cache(maxsize=1000)
def deep(x, n, i, last):
    print(f'STATUS: x: {x}, n: {n}, i: {i}, last: {last}')
    if i == 3: return 1
    if not x: return 0
    # special case: triplet empty
    if is_power(x[0], n) > -1 and last == None:
        return deep(x[1:], n, i+1, x[0]) + deep(x[1:], n, i, last)
    # general case
    if is_power(x[0], n) > -1 and is_power(x[0], n) - is_power(last, n) == 1:
        return deep(x[1:], n, i+1, x[0]) + deep(x[1:], n, i, last)
    else:
        return deep(x[1:], n, i, last)

def countTriplets(x, n):
    """the stack frames are not enought for gigantic amounts of data...
    """
    x = tuple(x)
    if not x or not n: return
    return deep(x, n, 0, None)


def countTriplets(arr, r):
    """one paass memory efficient way
    we will prepare counters for the next possible element,
    and when the next element arrives we accumulate the ocurrences of the previous matches
    """
    c_2, c_3 = Counter(), Counter()
    n_triplets = 0
    for e in arr:
        # print(f'arr: {arr}, e: {e}, c_3: {c_3}, c_2: {c_2}, n_triplets: {n_triplets}')
        if e in c_3:
            n_triplets += c_3[e]
        if e in c_2:
            c_3[e*r] += c_2[e]
        c_2[e*r] += 1
    return n_triplets

# test
# test = (1,2,2,4)
# n = 2
test = (1,3,9,9,27,81)
n = 3
print(f'testing with: {test}')
print(f'ans: {countTriplets(test,n)}')
