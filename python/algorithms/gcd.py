"""https://en.wikipedia.org/wiki/Euclidean_algorithm
find the greatest common factor
"""
def gcd(x, y):
    if y == 0: return x
    return gcd(y, x%y)
