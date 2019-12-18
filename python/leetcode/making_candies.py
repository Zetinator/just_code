"""https://www.hackerrank.com/challenges/making-candies/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=search

Karl loves playing games on social networking sites. His current favorite is CandyMaker, where the goal is to make candies.

Karl just started a level in which he must accumulate  candies starting with  machines and  workers. In a single pass, he can make  candies. After each pass, he can decide whether to spend some of his candies to buy more machines or hire more workers. Buying a machine or hiring a worker costs  units, and there is no limit to the number of machines he can own or workers he can employ.

Karl wants to minimize the number of passes to obtain the required number of candies at the end of a day. Determine that number of passes.
"""
from functools import lru_cache
import sys
sys.setrecursionlimit(10000)

def minimumPasses(m, w, p, n):
    """dynamic program approach
    """
    minimumPasses.min_passes = float('inf')

    @lru_cache(maxsize=None)
    def r(m,w,keep, p, n, passes=0):
        # do not explore further
        if passes >= minimumPasses.min_passes: return float('inf')
        # base cases
        candies = m*w + keep
        if n - candies <= 0:
            minimumPasses.min_passes = passes
            return passes
        # print(f'STATUS: (m: {m},w: {w}, keep: {keep}, p: {p}, n: {n}, passes: {passes}')
        # if n - candies <= 0: return (passes, (m,w,p,n))  # traceback
        # action time...
        res = []
        for i_m in range(candies+1):
            for i_w in range(i_m, candies+1):
                mm = i_m//p
                ww = (i_w - i_m)//p
                keep = candies - i_w
                res.append(r(m+mm, w+ww, keep, p, n, passes+1))
        return min(res)
        # return min(res) + ((m,w,p,n),)  # traceback
    return r(m,w,0, p,n, 1)


from collections import namedtuple

def minimumPasses(m, w, p, goal):
    """lets get greedy
    bsf approach...
    passed half of the 50 test cases
    """
    # set-up
    Node = namedtuple('node',['m','w','save'])
    initial_state = Node(m, w, 0)
    frontier = []
    frontier.append(initial_state)
    passes = 1
    while frontier:
        current_node = frontier.pop()
        # no revisiting
        # prepare next layer
        _next = []
        # greedy: buy resources until 2(m*w) >= n
        # print(f'STATUS: (m: {current_node.m},w: {current_node.w}, save: {current_node.save}, passes: {passes}')
        candies = current_node.m * current_node.w + current_node.save
        if candies+current_node.save >= goal: return passes
        if 2*candies+current_node.save >= goal: return passes+1
        if 3*candies+current_node.save >= goal: return passes+2
        # balance resources
        m, w, save = current_node.m, current_node.w, 0
        while candies//p > 0:
            candies -= p
            if current_node.m > current_node.w:
                w += 1
            else:
                m += 1
        save = candies
        _next.append(Node(m,w,save))
        frontier = _next
        passes += 1
    raise ValueError('What are you looking at...')

from math import ceil
def minimumPasses(machine, worker, p, n):
    # special case: goal is less than cost of upgrades
    if n <= p: return ceil(n/(machine * worker))
    # general case
    curr, candy = 0, 0
    minima = float('inf')
    while candy < n:
        # not enough for upgrades? fast forward...
        if candy < p:
            skip = ceil((p - candy)/(machine*worker))
            curr += skip
            candy += machine*worker*skip
            continue
        spend, candy = divmod(candy, p)
        # balance the resources
        for _ in range(spend):
            if machine > worker:
                worker += 1
            else:
                machine += 1
        # next round...
        curr += 1
        candy += machine * worker
        # predict how many runs will take us, with the current settings
        minima = min(minima, curr + ceil((n - candy)/(machine*worker)))
    return min(minima, curr)

test = [3, 1, 2, 12]
test = [1,1,6,45]
print(f'testing with: (machines, workers, cost, goal) {test}')
print(f'ans: {minimumPasses(*test)}')
