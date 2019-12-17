"""https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=greedy-algorithms

Complete the minimumAbsoluteDifference function in the editor below. It should return an integer that represents the minimum absolute difference between any pair of elements.

minimumAbsoluteDifference has the following parameter(s):

n: an integer that represents the length of arr
arr: an array of integers
"""

def minimumAbsoluteDifference(arr):
    """returns the minimum abs(delta) between sorted elements
    """
    arr = sorted(arr)
    minima = float('inf')
    for i in range(len(arr)-1):
        delta = abs(arr[i] - arr[i+1])
        if delta < minima: minima = delta
    return minima

# test
test = [1, -3, 71, 68, 17]
print(f'testing with: {test}')
print(f'ans: {minimumAbsoluteDifference(test)}')
