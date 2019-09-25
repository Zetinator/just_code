def largest_subarray(A,K):
    def kompare_arrays(x, y):
        for i, e in enumerate(x):
            if x[i] > y[i]:
                return x
        return y
    def get_subarrays(A,K):
        arrays = []
        for i in range(len(A)-K+1):
            arrays.append(A[i:i+K])
        return arrays
    def get_max_subarray(x):
        max_subarray = x[0]
        for e in x:
            max_subarray = e if kompare_arrays(max_subarray,e) else max_subarray
        return max_subarray
    # action time
    sub_arrays = get_subarrays(A,K)
    return get_max_subarray(sub_arrays)

# test
A = [1, 4, 3, 2, 5]
K = 4
print('test with: A={} and K={}'.format(A,K))
print(largest_subarray(A,K))
