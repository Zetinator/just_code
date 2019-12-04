"""
Given an int array nums of length n. Split it into strictly decreasing subsequences. Output the min number of subsequences you can get by splitting.

Input: [5, 2, 4, 3, 1, 6]
Output: 3
Explanation:
You can split this array into: [5, 2, 1], [4, 3], [6]. And there are 3 subsequences you get.
Or you can split it into [5, 4, 3], [2, 1], [6]. Also 3 subsequences.
But [5, 4, 3, 2, 1], [6] is not legal because [5, 4, 3, 2, 1] is not a subsuquence of the original array.
"""
def sub_decreasing(x: 'array with integers') -> 'min number of subsequences':
    def subarray(x, ans):
        if not x: return ans
        tmp = []
        for i,e in enumerate(x):
            if ans[-1][-1] > x[i]:
                ans[-1].append(x[i])
            else:
                tmp.append(x[i])
        print(f'STATUS: x:{x}, ans:{ans}, tmp:{tmp}')
        if not tmp: return ans
        return subarray(tmp[1:], ans + [[tmp[0]]])
    return subarray(x[1:], [[x[0]]])

# test
# test = [5, 2, 4, 3, 1, 6]
test = [2, 9, 12, 13, 4, 7, 6, 5, 10]
print(f'testing with: {test}')
print(f'ANS: {sub_decreasing(test)}')
