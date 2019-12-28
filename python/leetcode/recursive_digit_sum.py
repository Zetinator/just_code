"""https://www.hackerrank.com/challenges/recursive-digit-sum/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=recursion-backtracking

We define super digit of an integer  using the following rules:

Given an integer, we need to find the super digit of the integer.

If  has only  digit, then its super digit is .
Otherwise, the super digit of  is equal to the super digit of the sum of the digits of .
"""

def superDigit(n, k):
    first = sum([int(d)*k for d in n])
    first = str(first)
    def r(n):
        if len(n) == 1: return n
        n = sum([int(d) for d in n])
        return r(str(n))
    return r(first)

n = '148'
k = 3
print(f'testing with n: {n}, k: {k}, ans: {superDigit(n,k)}')

