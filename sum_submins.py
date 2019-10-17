"""
Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.
Input: [3,1,2,4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.
"""
def sum_submins(x: 'array of integers') -> 'sum of mins of subarrays':
    def min_substrings_k(x, k, ans):
        print(f'STATUS: x:{x}, k:{k}, ans:{ans}')
        if len(x) < k: return ans
        if not ans: return min_substrings_k(x[1:], k, [min(x[:k])])
        ans.append(min(x[:k]))
        return min_substrings_k(x[1:], k, ans)
    ans = []
    for i in range(1,len(x)+1):
        ans = ans + min_substrings_k(x, i, [])
    return sum(ans) % (10**9 + 7)

# test
test = [3,1,2,4]
print(f'testing with: {test}')
print(f'ANS: {sum_submins(test)}')