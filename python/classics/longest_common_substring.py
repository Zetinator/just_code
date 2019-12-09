"""In computer science, the longest common substring problem is to find the longest string (or strings) that is a substring (or are substrings) of two or more strings.

https://en.wikipedia.org/wiki/Longest_common_substring_problem
"""
from functools import lru_cache


@lru_cache(maxsize=1000)
def r(x, y, record=0):
    """recursive implementation
    """
    if not x or not y: return record
    # print(f'STATUs: x: {x}, y: {y}, record: {record}')
    if x[0] == y[0]:
        return max(record, r(x[1:], y[1:], record+1))
    return max(record, r(x, y[1:], 0), r(x[1:], y, 0))

def lcs(x, y):
    """returns the longest common substring in O(N*M)
    """
    if not x or not y: return 0
    return r(x, y)

# test 
e = 'kim es super bonita'
m = 'erick es lo maximo'
print(f'testing with: {e}, {m}') 
print(f'ans: {lcs(e, m)}')
