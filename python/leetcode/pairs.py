"""https://www.hackerrank.com/challenges/pairs/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=search

You will be given an array of integers and a target value. Determine the number of pairs of array elements that have a difference equal to a target value.
Complete the pairs function below. It must return an integer representing the number of element pairs having the required difference.

pairs has the following parameter(s):

    k: an integer, the target difference
    arr: an array of integers.
"""
from collections import Counter

def pairs(k, arr):
    counter = Counter()
    n_pairs = 0
    for e in arr:
        # print(f'e: {e}, counter: {counter}, n_pairs: {n_pairs}')
        if e in counter:
            n_pairs += counter[e]
        counter[e+k] += 1
        counter[e-k] += 1
    return n_pairs

# test
k = 2
arr = [1,3,5,8,6,4,2]
print(f'testing with: {arr}')
print(f'ans: {pairs(k, arr)}')
