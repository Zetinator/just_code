def deep_select(x, k):
    pivot = x[0]
    minor = [e for e in x[1:] if e < pivot]
    mayor = [e for e in x[1:] if e > pivot]
    print(f'STATUS: x:{x}, k:{k}, pivot:{pivot}')
    if k == len(minor): return pivot
    if k < len(minor):
        return deep_select(minor, k)
    else:
        return deep_select(mayor, (k-1)-len(minor))  # - pivot and - len(minor)

# test
# test = [1, 3, 2, 6, 5, 2, 5, 0]
test = [3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]
print(f'testing with: {test}')
print(f'ordered: {sorted(test)}')
print(f'ANS: {deep_select(test, len(test)//2)}')
