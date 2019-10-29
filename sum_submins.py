"""
Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.
Input: [3,1,2,4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.
"""
def sum_submins(x: 'array of integers') -> 'sum of mins of subarrays':
    ans = []
    for i in range(len(x)):
        for j in range(i+1,len(x)+1):
            ans.append(min(x[i:j]))
    return sum(ans)

# test
test = [3,1,2,4]
print(f'testing with: {test}')
print(f'ANS: {sum_submins(test)}')
