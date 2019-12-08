def deep_sort(x):
    if not x: return []
    pivot = x[0]
    minor = deep_sort([e for e in x[1:] if e < pivot])
    mayor = deep_sort([e for e in x[1:] if e >= pivot])
    return minor + [pivot] + mayor

def bs(x, val):
    _from, _to = 0, len(x)-1
    while _from < _to:
        m = (_from + _to)//2
        if x[m] == val: return m
        if val < x[m]:
            _to = m
        else:
            _from = m+1
    raise ValueError(f'{val} not found')

# recursive
def r_bs(x, v):
    def deep(x, v, n):
        print(f'STATUS: x:{x}, n:{n}')
        if not x: raise KeyError(f'{v}: NOT FOUND')
        if x[len(x)//2] == v: return n
        if x[len(x)//2] < v:
            right = x[len(x)//2+1:]
            return deep(right, v, n - (-len(right)//2))
        else:
            left = x[:len(x)//2]
            return deep(left, v, n + (-len(left)//2))
    return deep(x, v, len(x)//2)

# test
test = [2, 3, 4, 5, 15, 19, 26, 27, 36, 38, 44, 46, 47, 48, 50]
val = 5
print(f'testing with: {test}, look for: {val}')
print(f'ANS: {bs(test, val)}')
