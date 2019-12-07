def deep_jump(x: 'the rest of the arrray', p: 'current pos', n: 'step') -> 'index where to land':
    if not x: 
        return 1
    if n % 2 == 0:
        index = x.index(max(x)) if p >= max(x) else None
        if index == None: return 0
        return deep_jump(x[index+1:], x[index], n+1)
    else:
        index = x.index(min(x)) if p <= min(x) else None
        if index == None: return 0
        return deep_jump(x[index+1:], x[index], n+1)
def odd_even_jump(x: 'input array') -> 'the number of good indexes':
    n = 0
    while x:
        n += deep_jump(x[1:], x[0], 1)
        x.pop(0)
    return n

# test
# test = [10,13,12,14,15]
# test = [2,3,1,1,4]
test = [5,1,3,4,2]
print(f'testing with: input:{test}')
# print(deep_jump(test[3+1:],test[3], 1))
print(odd_even_jump(test))
