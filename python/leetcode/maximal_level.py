def _sum(x):
    ans = []
    for e in x:
        n = sum([i for i in e if i])
        ans.append(n)
    return ans
def get_subarrays(x):
    def deep(x, sub_arrays, n):
        if x == []: return sub_arrays
        sub_arrays.append(x[:2**(n)])
        return deep(x[2**(n):], sub_arrays, n+1)
    sub_arrays = []
    return deep(x, sub_arrays, 0)
def maximal_level(x):
    _ = _sum(get_subarrays(x))
    level = _.index(max(_))
    return level

# test
test = [1,7,0,7,-8,None,None]
print('testing with: {}'.format(test))
print(maximal_level(test))
