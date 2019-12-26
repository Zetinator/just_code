"""https://www.hackerrank.com/challenges/poisonous-plants/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues

There are a number of plants in a garden. Each of these plants has been treated with some amount of pesticide. After each day, if any plant has more pesticide than the plant on its left, being weaker than the left one, it dies.

You are given the initial values of the pesticide in each of the plants. Print the number of days after which no plant dies, i.e. the time after which there are no plants with more pesticide content than the plant to their left.
"""
import sys
sys.setrecursionlimit(100000)

def poisonousPlants(p):
    """naive solution, recursive
    almost there, failing because of recursion depth
    """
    def r(x, ans=0):
        tmp = [x[0]]
        for i in range(len(x)-1):
            if x[i] >= x[i+1]: tmp.append(x[i+1])
        if tmp == x: return ans
        return r(tmp, ans+1)
    return r(p)

def poisonousPlants(p):
    """naive solution, iterative
    not fast enought...
    """
    for days in range(len(p)):
        tmp = p[:1]
        for i in range(len(p)-1):
            if p[i] >= p[i+1]: tmp.append(p[i+1])
        if p == tmp: return days
        p = tmp

from collections import deque

def poisonousPlants(p):
    """stack solution...
    the solution is a list of stacks
    working... almost
    """
    # create list of stacks in descendent order
    stacks = []
    tmp = deque(p[:1])
    for i in range(len(p)-1):
        if p[i] < p[i+1]:
            stacks.append(tmp)
            tmp = deque([p[i+1]])
        else:
            tmp.append(p[i+1])
    # push the remaining
    stacks.append(tmp)
    if len(stacks[0]) == len(p): return 0
    print(f'stacks: {stacks}')
    for days in range(1, len(p)):
        current_min = stacks[0][-1]
        pop_flag = False
        for stack in stacks[1:]:
            if not stack: continue
            print(f'day: {days}, stack: {stack}, current_min: {current_min}')
            while stack and stack[0] > current_min:
                print(f'deque: {stack[0]}')
                stack.popleft()
                pop_flag = True
            current_min = stack[-1] if stack else current_min
        if not pop_flag: return days

from collections import deque
def poisonousPlants(p):
    """optimized solution
    """
    # create list of stacks
    stacks, days = [deque(p[:1])], 0
    for i, v in enumerate(p[1:], 1):
        if p[i-1] < v: stacks += [deque([v])]
        else: stacks[-1] += [v]
    # consecutive pops according to the days
    while len(stacks) > 1:
        i = 1
        while i < len(stacks):
            stacks[i].popleft()
            if not stacks[i]: stacks.pop(i)
            elif stacks[i-1][-1] >= stacks[i][0]:
                stacks[i-1] += stacks[i]
                stacks.pop(i)
            else: i += 1
        days += 1
    return days

# test
test = [6,5,8,4,7,10,9]
test = [4, 3, 7, 5, 6, 4, 2,]
# test = [3,2,5,4]
print(f'testing with {test}')
print(f'ans: {poisonousPlants(test)}')
