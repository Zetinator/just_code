"""https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

Complete the function hourglassSum in the editor below. It should return an integer, the maximum hourglass sum in the array.
"""

def hourglassSum(arr):
    """given the 6x6 array extract all the hourglasses avalible and retrieve the max
    """
    # special case: empty
    if not arr or not arr[0]: return
    # special case: not hourglass possible
    if len(arr) < 3 or len(arr[0]) < 3: return
    # general case
    hourglasses =[]
    for i in range(len(arr)-2):
        for j in range(len(arr[0])-2):
            up = [arr[i][j],arr[i][j+1],arr[i][j+2]]
            middle = [arr[i+1][j+1]]
            down = [arr[i+2][j],arr[i+2][j+1],arr[i+2][j+2]]
            hourglasses.append(sum(up + middle + down))
    return max(hourglasses)


# test
test = [[1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0]]
print(f'input: ')
for line in test: print(line)
print(f'ans: {hourglassSum(test)}')
