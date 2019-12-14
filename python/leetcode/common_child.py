"""https://www.hackerrank.com/challenges/common-child/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=strings

A string is said to be a child of a another string if it can be formed by deleting 0 or more characters from the other string. Given two strings of equal length, what's the longest string that can be constructed such that it is a child of both?
"""
from functools import lru_cache

def commonChild(s1, s2):
    """dynamic programming approach
    unfortunately not executing within the time limits, almost though :(
    """
    @lru_cache(maxsize=None)
    def r(x, y, max_child=0):
        if not x or not y: return max_child
        # print(f'x: {x}, y: {y}, max_child: {max_child}')
        if x[0] == y[0]: return r(x[1:], y[1:], max_child+1)
        return max(r(x, y[1:], max_child), r(x[1:], y, max_child))
    return r(s1, s2)

def commonChild(s1, s2):
    """dynamic programming approach
    not passing the strings but just indexes, fails because of recursion depth reached
    """
    strings = [s1, s2]
    def recurse(l, r, max_child=0):
        if not l<len(strings[0]) or not r<len(strings[1]): return max_child
        # print(f'x: {strings[0][l]}, y: {strings[1][r]}, max_child: {max_child}')
        if strings[0][l] == strings[1][r]: return recurse(l+1, r+1, max_child+1)
        return max(recurse(l, r+1, max_child), recurse(l+1, r, max_child))
    return recurse(0, 0)

def commonChild(X, Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)

    # declaring the array for storing the dp values
    L = [[None]*(n+1) for i in range(m+1)]

    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])

    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L



# test
a = 'SHINCHAN'
b = 'NOHARAAA'
print(f'testing with: a:{a}, b:{b}')
l = commonChild(a,b)
for e in l: print(e)
# print(f'ans: {commonChild(a, b)}')

