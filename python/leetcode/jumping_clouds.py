"""
Emma is playing a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. She can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus 1 or 2. She must avoid the thunderheads.
"""
def deep(x, jumps):
    if not x or len(x) == 1: return jumps
    print(f'STATUS: x: {x}, jumps: {jumps}')
    if x[0] == 1: return float('inf')
    return min(deep(x[1:], jumps+1), deep(x[2:], jumps+1))

def play(x):
    return deep(x, 0)


# test
# test = [0, 0, 1, 0, 0, 1, 0]
test = [0,0,0,1,0,0]
print(f'testing with: {test}')
print(f'ans: {play(test)}')
