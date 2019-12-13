"""https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=arrays

You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates. You are allowed to swap any two elements. You need to find the minimum number of swaps required to sort the array in ascending order.
"""

def minimumSwaps(x):
    right_pos = {e: i for i, e in enumerate(sorted(x))}
    def entropy(x, right_pos):
        return sum([abs(i-right_pos[e]) for i,e in enumerate(x)])
    swaps = 0
    while entropy(x, right_pos) != 0:
        swaps += 1
        minima = min([i for i in range(len(x))], key=lambda i: i-right_pos[x[i]])
        maxima = max([i for i in range(minima, len(x))], key=lambda i: i-right_pos[x[i]])
        x[minima], x[maxima] = x[maxima], x[minima]
    return swaps

test = [7, 1, 3, 2, 4, 5, 6]
# test = [2, 1, 3, 7, 4, 5, 6]
# test = [1, 2, 3, 7, 4, 5, 6]
# test = [1, 2, 3, 4, 7, 5, 6]
# test = [1, 2, 3, 4, 5, 7, 6]
# test = [1, 2, 3, 4, 5, 6, 7]
print(f'testing with: {test}')
print(f'ans: {minimumSwaps(test)}')
