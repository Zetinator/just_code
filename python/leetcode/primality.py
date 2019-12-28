"""https://www.hackerrank.com/challenges/ctci-big-o/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=miscellaneous

Complete the primality function in the editor below. It should return Prime if  is prime, or Not prime.
"""

def primality(n):
    if n <= 3: return 'Prime' if n > 1 else 'Not prime'
    if n%2 == 0 or n%3 == 0: return 'Not prime'
    # 6k + 1 optimization 
    i = 5
    while i**2 <= n:
        if n%i == 0 or n%(i+2) == 0: return 'Not prime'
        i += 6
    return 'Prime'

# test
test = 53
print(f'is {test} prime ans: {primality(test)}')
