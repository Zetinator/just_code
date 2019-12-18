"""https://www.hackerrank.com/challenges/triple-sum/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=search

Complete the triplets function in the editor below. It must return the number of distinct triplets that can be formed from the given arrays.

triplets has the following parameter(s):

a, b, c: three arrays of integers .
"""
def triplets(a, b, c):
    # keep unique elements
    a = list(set(a))
    b = list(set(b))
    c = list(set(c))
    # timsort
    a.sort(); b.sort(); c.sort()
    n_triplets = 0
    # execute 'inclusive' binary search on the sorted arrays
    def bs(arr, value):
        l, r = 0, len(arr)
        while l < r:
            m = (l+r)//2
            if arr[m] == value: return m+1
            if value < arr[m]:
                r = m
            else:
                l = m+1
        return l
    for e in b:
        i_a = bs(a, e)
        i_c = bs(c, e)
        n_triplets += i_a * i_c
    return n_triplets

# test
a = [1,3,5,7]
b = [5,7,9]
c = [7,9,11,13]
a = [3,5,7]
b = [3,6]
c = [4,6,9]
print(f'testing with: {a}, {b}, {c}')
print(f'ans: {triplets(a,b,c)}')
