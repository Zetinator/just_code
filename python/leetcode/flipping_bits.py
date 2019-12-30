"""https://www.hackerrank.com/challenges/flipping-bits/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=miscellaneous

You will be given a list of 32 bit unsigned integers. Flip all the bits ( and ) and print the result as an unsigned integer.
"""

def flippingBits(n):
    """easy piece...
    """
    return n^(2**32-1)
