def deep_sort(x):
    if not x: return []
    pivot = x[0]
    minor = deep_sort([e for e in x[1:] if e < pivot])
    mayor = deep_sort([e for e in x[1:] if e >= pivot])
    return minor + [pivot] + mayor

def bs(x, v):
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
# test = [1, 3, 2, 6, 5, 2, 5, 0]
test = [3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]
print(f'testing with: {test}')
test = deep_sort(test)
print(f'ordered: {test}')
print('ANS: {}'.format(bs(test, 5)))
