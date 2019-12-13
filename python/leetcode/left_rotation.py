"""https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&h_r=next-challenge&h_v=zen&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=arrays

A left rotation operation on an array shifts each of the array's elements 1 unit to the left. 
"""

def rotLeft(arr, n=0):
    """rotate left 'n' times the given array
    """
    n = n%len(arr)
    return arr[n:] + arr[:n]

# test
test = [ i for i in range(10)]
n = 3
print(f'input: arr: {test}, n: {n}')
print(f'ans: {rotLeft(test, n)}')

