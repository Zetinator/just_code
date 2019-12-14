"""https://www.hackerrank.com/challenges/ctci-merge-sort/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=sorting

Given d datasets, print the number of inversions that must be swapped to sort each dataset on a new line.
"""

# passed almost all tests, maybe an overflow somewhere
def countInversions(x):
    def r(x):
        if not x: return 0
        n = len([e for e in x[1:] if e < x[0]])
        return n + r(x[1:])
    return r(x)

# naive implementation... timeout
def countInversions(x):
    n = 0
    for i, e in enumerate(x):
        for j in range(i, len(x)):
            if e > x[j]: n += 1
    return n

def countInversions(x):
    total_invertions = [0]
    # standard recursive merge sort...
    def recurse(x):
        # base case
        if len(x) == 1: return x
        # standard divide
        m = len(x)//2
        left = recurse(x[:m])
        right = recurse(x[m:])
        # almost standard conquer
        l, r = 0, 0
        res = []
        while l<len(left) and r<len(right):
            if left[l] <= right[r]:
                res.append(left[l])
                l += 1
            else:
                res.append(right[r])
                r += 1
                # here es the magic...
                # add the current size of left
                total_invertions[0] += len(left) - l
        while l<len(left):
            res.append(left[l])
            l += 1
        while r<len(right):
            res.append(right[r])
            r += 1
        return res
    recurse(x)
    return total_invertions[0]

# test
test = [2, 1, 3, 1, 2]
# test = [7, 5, 3, 1]
print(f'testing with: {test}')
print(f'ans: {countInversions(test)}')
