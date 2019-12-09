"""the ugly numbers
https://www.geeksforgeeks.org/ugly-numbers/
"""
from math import log
from functools import lru_cache
@lru_cache(maxsize=512)
def check_base(number: int, base: int=2) -> int:
    """check if the number is divisible by 'base'
    """
    if number % base != 0: return number
    return check_base(number/base, base)

def ugly_number(n):
    """returns the n'th ugly number
    ugly numbers are numbers whose only prime factors are 2, 3 or 5
    by convention, 1 is included.
    """
    bases = [2, 3, 5]
    normal_number_counter = 1
    ugly_number_counter = 0
    current_ugly = 0
    while ugly_number_counter < n:
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
print(f'the {n}th ugly number is: {ugly_number(n)}')
