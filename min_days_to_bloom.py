"""
Given an array of roses. roses[i] means rose i will bloom on day roses[i]. Also given an int k, which is the minimum number of adjacent bloom roses required for a bouquet, and an int n, which is the number of bouquets we need. Return the earliest day that we can get n bouquets of roses.

Example:
    Input: roses = [1, 2, 4, 9, 3, 4, 1], k = 2, n = 2
    Output: 4
    Explanation:
    day 1: [b, n, n, n, n, n, b]
    The first and the last rose bloom.

    day 2: [b, b, n, n, n, n, b]
    The second rose blooms. Here the first two bloom roses make a bouquet.

    day 3: [b, b, n, n, b, n, b]

    day 4: [b, b, b, n, b, b, b]
    Here the last three bloom roses make a bouquet, meeting the required n = 2 bouquets of bloom roses. So return day 4.
"""
def days_to_bloom(x: 'array with fowers to bloom',
                  k: 'flowers per bouquet',
                  n: 'number of bouquets to fill') -> 'days to fill':
    subarrays = []
    for i in range(len(x)-(k-1)):
        subarray = []
        for j in range(k):
            subarray.append(x[i+j])
        subarrays.append(subarray)
    subarrays = sorted(subarrays, key=lambda x: sum(x))
    ans = 0
    for e in subarrays[:n]:
        if max(e) > ans: ans = max(e)
    return ans

# test
roses = [1, 2, 4, 9, 3, 4, 1]
k = 2
n = 2
print(f'testing with: {roses}')
print(f'ANS: {days_to_bloom(roses, k ,n)}')
