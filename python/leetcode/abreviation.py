"""https://www.hackerrank.com/challenges/abbr/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=dynamic-programming

You can perform the following operations on the string, :

Capitalize zero or more of 's lowercase letters.
Delete all of the remaining lowercase letters in .
Given two strings,  and , determine if it's possible to make  equal to  as described. If so, print YES on a new line. Otherwise, print NO.

For example, given  and , in  we can convert  and delete  to match . If  and , matching is not possible because letters may only be capitalized or discarded, not changed.
"""

def abbreviation(a, b):
    """dynamic programming
    """
    s_b = set(b)
    for i, x in enumerate(a):
        if x not in s_b: return 'NO'
        for j, y in enumerate(b):
            pass
    return

from functools import lru_cache
import sys
sys.setrecursionlimit(100000)

def abbreviation(a, b):
    """dynamic programming
    almost...
    """
    @lru_cache(maxsize=None)
    def r(x,y):
        # we are done
        if not y and not x: return True
        # if they match, no options we take it...
        if x and y and x[0] == y[0]: return r(x[1:], y[1:])
        # if they partially match, we can make it uppercase or 'delete' it
        if x and y and x[0].upper() == y[0]:
            return r(x[1:], y[1:]) or r(x[1:], y)
        # if is lowercase we can 'delete' it
        if x and x[0].islower(): return r(x[1:], y)
    return 'YES' if r(a, b) else 'NO'

a = 'abcdefghijklmnopqrstuvwxyzababababAbAbaBabAbababababAbababaBabaBabAbaBababababababababaBababaBababababaBabaBabababABabababAbabababaBAbababababababababababAbababaBabababAbabababababababaBaBabAbabaBababababababababaBAbabaBAbabAbababababaBababAbababababababaBabababababaBaBaBababababAbabaBababaBaBabababababababababababababababababababAbababababababababAbababaBababababababababAbabaBabababaBAbabababababababababababababababaBababAbabababaBAbababababaBabababababababaBaBabababababababAbababababababababAbabababaBabAbabaBabAbAbabAbaBabababababaBaBababABabababababAbaBababababababaBabababababababababababAbababababababababababababababababaBabababababababababababababababAbabaBababababababababababaBAbabababAbababababababababaBabababaBaBabababababababababaBababAbaBababAbababababaBAbababaBababababababAbABabababAbababaBababababababaBaBababababAbAbabababababababababaBababababababababababababababababaBabababAbabAbababababABabababAbabababababababababaBabABCDEFGHIJKLMNOPQRSTUVWXYZ'
b = 'ABCDEFGHIJKLMNOPQRSTUVWXYZAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(f'testing with: a: {a}, b: {b}')
print(f'ans: {abbreviation(a, b)}')
