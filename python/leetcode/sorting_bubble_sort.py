"""https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=sorting

Given an array of integers, sort the array in ascending order using the Bubble Sort algorithm above. Once sorted, print the following three lines:

Array is sorted in numSwaps swaps., where  is the number of swaps that took place.
First Element: firstElement, where  is the first element in the sorted array.
Last Element: lastElement, where  is the last element in the sorted array.
"""

def countSwaps(x):
    swaps = 0
    for i in x:
        for j in range(len(x)-1):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
                swaps += 1
    print(f'Array is sorted in {swaps} swaps.')
    print(f'First Element: {x[0]}')
    print(f'Last Element: {x[-1]}')

# test
test = [33, 66, 1, 65, 5, 7, 41, 74, 11, 45, 14, 60, 48, 84, 85, 31, 93, 63]
print(f'testing with: {test}')
print(f'ans: {countSwaps(test)}')
