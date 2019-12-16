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

def commonChild(s1, s2):
    """botton-up approach, classic
    """
    table = [[0]*(len(s1)+1) for _ in range(len(s2)+1)]
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                table[i][j] = table[i-1][j-1]+1
            else:
                table[i][j] = max(table[i-1][j] , table[i][j-1])
    return table[i][j]

def commonChild(s1, s2):
    """bottom-up approach memory efficient
    uses just a row and the last column value
    """
    last_row = [0]*(len(s1)+1)
    for i in range(1, len(s1)+1):
        current = [0]
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                current.append(last_row[j-1]+1)
            else:
                current.append(max(last_row[j] , current[-1]))
        last_row = current
    return last_row[-1]

# test
a = 'SHINCHAN'
b = 'NOHARAAA'
print(f'testing with: a:{a}, b:{b}')
l = commonChild(a,b)
print(f'ans: {commonChild(a, b)}')

