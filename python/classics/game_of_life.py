"""Game of life on an array...
Every cell interacts with its two neighbours, which are the cells that are adjacent. At each step in time, the following transitions occur:

Any live cell with fewer than 1 live neighbours dies, as if by underpopulation.
Any live cell with 1 live neighbours lives on to the next generation.
Any live cell with more than one live neighbours dies, as if by overpopulation.

https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
"""
def xor(x, y):
    """custom implementation of the missing xor function
    """
    return int(bool(x) != bool(y))

def r(state, n):
    """recursive implementation
    """
    # base case
    if not n: return state
    # general case
    head, tail = xor(0, state[1]), xor(0, state[-2])
    body = []
    for i in range(len(state)):
        # we skip head and tail for they were already computed
        if i == 0 or i == len(state)-1: continue
        body.append(xor(state[i-1], state[i+1]))
    return r([head] + body + [tail], n-1)

def game_of_life(state, n):
    if not state: return
    return r(state, n)

# test
state = [1,0,1,1,0,1,0,1,0,0,0,1,1]
n = 5
print(f'testing with: state: {state}, after: {n} days')
print(f'ANS: {game_of_life(state,n)}')
