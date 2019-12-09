"""
Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.
Input: [3,1,2,4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.
"""
def sum_submins(x: list) -> int:
    """returns the sum of the min's in all possible substrings
    """
    ans = []
    # get all substrings
    for i in range(len(x)):
        for j in range(i,len(x)):
            ans.append(min(x[i:j+1]))
    return sum(ans)

# test
test = [3,1,2,4]
print(f'testing with: {test}')
print(f'ANS: {sum_submins(test)}')
