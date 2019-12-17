"""https://www.hackerrank.com/challenges/angry-children/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=greedy-algorithms

Complete the maxMin function in the editor below. It must return an integer that denotes the minimum possible value of unfairness.

maxMin has the following parameter(s):

k: an integer, the number of elements in the array to create
arr: an array of integers .
"""

def maxMin(k, arr):
    s_arr = sorted(arr)
    minima = float('inf')
    for i in range(len(s_arr)-(k-1)):
        # the begining is inclusive and the end is exclusive
        print(f'max: {s_arr[i+(k-1)]}, min: {s_arr[i]}')
        delta = s_arr[i+(k-1)] - s_arr[i]
        if delta < minima: minima = delta
    return minima

# test
k = 4
arr = [1,
        2,
        3,
        4,
        10,
        20,
        30,
        40,
        100,
        200]
print(f'testing with: {arr}')
print(f'ans: {maxMin(k, arr)}')

