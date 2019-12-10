"""bit mask operations
https://visualgo.net/en/bitmask
"""

def set(state, i):
    return state|(1<<i)

def reset(state, i):
    set(state, i)
    return toggle(state, i)

def toggle(state, i):
    return state^(1<<i)

def check(state, i):
    return bool(state&(1<<i))

def clear(self):
    return state&0
