from math import log
from functools import lru_cache
@lru_cache(maxsize=512)
def check_base(number:'number to check',
                base: int = 2) -> 'residual':
    if number % base != 0: return number
    return check_base(number/base, base)

def ugly_number(n):
    bases = [2, 3, 5]
    normal_number_counter = 1
    ugly_number_counter = 0
    current_ugly = 0
    while ugly_number_counter < n:
        print('STATUS: normal_number_counter: {}, ugly_number_counter: {}, current_ugly: {}'.format(
                normal_number_counter, ugly_number_counter, current_ugly))
        _ = normal_number_counter
        for base in bases:
            _ = check_base(_, base)
            if _ == 1:
                current_ugly = normal_number_counter
                ugly_number_counter += 1
                break
        normal_number_counter += 1
    return current_ugly

# test
n = 150
print('testing with {}'.format(n))
print(ugly_number(n))
