"""Game of life on an array...
"""
def xor(x, y):
    return int(bool(x) != bool(y))

def deep(s, n):
    if not n: return s
    print(f'STATUS: s: {s}, n: {n}')
    head = xor(0, s[1])
    tail = xor(0, s[-2])
    body = []
    for i,e in enumerate(s):
        if i == 0 or i == len(s)-1: continue
        body.append(xor(s[i-1], s[i+1]))
    return deep([head] + body + [tail], n-1)

def game_of_life(s, n):
    if not s: return
    return deep(s, n)

# test
s = [1,0,1,1,0,1,0]
n = 2
print(f'testing with: s: {s}, n: {n}')
print(f'ANS: {game_of_life(s,n)}')
