"""https://www.hackerrank.com/challenges/luck-balance/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=greedy-algorithms

Complete the luckBalance function in the editor below. It should return an integer that represents the maximum luck balance achievable.

luckBalance has the following parameter(s):

k: the number of important contests Lena can lose
contests: a 2D array of integers where each  contains two integers that represent the luck balance and importance of the  contest.
"""
from functools import lru_cache

def luckBalance(k, contests):
    """dynamic programming solution working 
    but reached the depth limit in the hackerrank compiler
    """
    contests = tuple(contests)

    # @lru_cache(maxsize=1024)
    def recurse(contests, k, max_luck):
        # special case: empty contest arrays
        if not contests: return max_luck
        print(f'contest: {contests}, k: {k}, max_luck: {max_luck}')
        # general case
        luck, importance = contests[0]
        if k - importance < 0:
            return recurse(contests[1:], k, max_luck-luck)  # she is forced to win the rest of the contests
        return max(recurse(contests[1:], k-importance, max_luck+luck),  # she either losses and wins luck
                    recurse(contests[1:], k, max_luck-luck))  # or she wins and losses luck
    return recurse(contests, k, 0)


def luckBalance(k, contests):
    """dynamic programming solution working 
    but reached the depth limit in the hackerrank compiler
    """
    # i can lose up to k times, then i will lose the k most valuable ones
    s_contests = sorted(contests, key= lambda x: (-x[1], -x[0]))
    max_luck = 0
    to_lose = s_contests[:k]
    max_luck = sum([luck for luck, importance in to_lose])
    for e in s_contests[k:]:
        luck, importance = e
        if importance:
            max_luck -= luck
        else:
            max_luck += luck
    return max_luck


# test
k = 3
test = [[5, 1],
        [2, 1],
        [1, 1],
        [8, 1],
        [10, 0],
        [5, 0]]
print(f'testing with:')
for line in test: print(line)
print(f'ans: {luckBalance(k, test)}')
