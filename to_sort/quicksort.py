# like quicksort but is the one i will implement... O(n*log(n))
def deep_sort(x):  #looks better, but slower (because needs to go through x twice)
    if not x: return []
    # print(f'STATUS: x:{x}')
    pivot = x[0]
    minor = deep_sort([e for e in x[1:] if e < pivot])
    mayor = deep_sort([e for e in x[1:] if e >= pivot])
    # print(f'STATUS: minor:{minor}, pivot:{pivot}, mayor{mayor}')
    return minor + [pivot] + mayor

def deep_sort_v1(x):  #slightly faster, more code
    if not x: return []
    # print(f'STATUS: x:{x}')
    pivot = x[0]
    minor = []
    mayor = []
    for e in x[1:]:
        if e < pivot:
            minor.append(e)
        else:
            mayor.append(e)
    minor = deep_sort_v1(minor)
    mayor = deep_sort_v1(mayor)
    return minor + [pivot] + mayor

# test
test = [3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]
import numpy as np
test = np.random.randint(1000, size=[1000])
test = list(test)
print('testing with: {}'.format(test))
print('ANS: {}'.format(deep_sort(test)))
