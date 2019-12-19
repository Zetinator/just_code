"""https://www.hackerrank.com/challenges/decibinary-numbers/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=dynamic-programming

Consider an infinite list of non-negative decibinary numbers that is sorted according to the following rules:

The decibinary numbers are sorted in increasing order of the decimal value that they evaluate to.
Any two decibinary numbers that evaluate to the same decimal value are ordered by increasing decimal value, meaning the equivalent decibinary values are strictly interpreted and compared as decimal values and the smaller decimal value is ordered first.

You will be given  queries in the form of an integer, . For each , find and print the the  decibinary number in the list on a new line.
"""

def decibinaryNumbers(x):
    return


test = [4, 6, 4, 5, 6, 2]
test = [1,2,2]
n = len(test)
print(f'testing with: {test}')
print(f'ans: {decibinary(test)}')

