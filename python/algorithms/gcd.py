"""https://en.wikipedia.org/wiki/Euclidean_algorithm
find the greatest common factor
"""
def gcd(x, y):
    if y == 0: return x
    return gcd(y, x%y)

# test
x = 9
y = 66
print(f'greatest common factor of {x} and {y} is: {gcd(x,y)}')

