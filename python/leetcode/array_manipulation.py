"""https://www.hackerrank.com/challenges/crush/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=arrays

Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each of the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in your array.
"""

# filling all the vector
def arrayManipulation(n, querys):
    """implementation filling the whole vector
    """
    x = [0]*n
    for q in querys:
        i, j, k = q
        x[i-1:j] = [e+k for e in x[i-1:j]]
        print(f'x: {x}')
    return max(x)

# min sums in the vector... avoids the memory overflow in hackerrank
def arrayManipulation(n, querys):
    """no overflows
    instead of filling the whole vector everytime it only sums the begining
    and at the end it substracts, that way the max of the cumulative sums is return
    """
    x = [0]*(n+1)
    for q in querys:
        i, j, k = q
        x[i-1] += k
        x[j] -= k
    acc, maxima = 0, 0
    for e in x:
        acc += e
        maxima = acc if maxima < acc else maxima
    return maxima

# test
n = 10
test = [[1, 5, 3],
        [4, 8, 7],
        [6, 9, 1]]
print(f'testing with:')
for line in test: print(line)
print(f'ans: {arrayManipulation(n, test)}')
