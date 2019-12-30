"""https://www.hackerrank.com/challenges/game-of-two-stacks/problem

Alexa has two stacks of non-negative integers, stack  and stack  where index  denotes the top of the stack. Alexa challenges Nick to play the following game:

In each move, Nick can remove one integer from the top of either stack  or stack .
Nick keeps a running sum of the integers he removes from the two stacks.
Nick is disqualified from the game if, at any point, his running sum becomes greater than some integer  given at the beginning of the game.
Nick's final score is the total number of integers he has removed from the two stacks.
Given , , and  for  games, find the maximum possible score Nick can achieve (i.e., the maximum number of integers he can remove without being disqualified) during each game and print it on a new line.
"""

from functools import lru_cache
def twoStacks(x, a, b):
    """dynamic programming approach
    not fast enought...
    """
    # build stacks...
    @lru_cache(maxsize=None)
    def r(status_stacks, x, acc):
        i, j = status_stacks 
        if x <= 0: return acc - 1
        # print(f'status: {status_stacks}, x: {x}, acc: {acc}')
        if i == len(a) and j == len(b): return len(a) + len(b)
        if i == len(a): return r((i, j+1), x-b[j], acc+1)
        if j == len(b): return r((i+1, j), x-a[i], acc+1)
        return max(r((i+1, j), x-a[i], acc+1),  # pull from a
                    r((i, j+1), x-b[j], acc+1))  # or from b
    return r((0,0), x, 0)

def twoStacks(x, a, b):
    """using cumulative sums...
    """
    if min(a[0], b[0]) > x: return 0
    acc_a, acc_b = a[:1], b[:1]
    # build the prefix sum arrays...
    for e in a[1:]:
        tmp = e + acc_a[-1]
        if tmp > x: break
        acc_a.append(tmp)
    for e in b[1:]:
        tmp = e + acc_b[-1]
        if tmp > x: break
        acc_b.append(tmp)
    # we keep the biggest one...
    if len(acc_a) < len(acc_b): acc_a, acc_b = acc_b, acc_a
    j, ans = 0, 0
    # maybe the combination is greater than the parts alone
    for i in reversed(range(len(acc_a))):
        while j < len(acc_b) and acc_a[i] + acc_b[j] <= x: j += 1
        ans = max(ans, i + j + 1)
    return ans

x = 10
a = """4 2 4 6 1"""
b = """2 1 8 5"""
a = [int(e) for e in a.split()]
b = [int(e) for e in b.split()]
print(f'from a: {a}, b: {b}, x: {x}, ans: {twoStacks(x, a, b)}')
