"""https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=strings

Sherlock considers a string to be valid if all characters of the string appear the same number of times. It is also valid if he can remove just  character at  index in the string, and the remaining characters will occur the same number of times. Given a string , determine if it is valid. If so, return YES, otherwise return NO.
"""
from collections import Counter

def isValid(s):
    counter = Counter(s).most_common()
    minima = counter.pop()[1]
    # special case: the minimum is 1
    if minima == 1:
        if not counter: return 'YES'
        minima = counter.pop()[1]
        for e in counter:
            repetitions = e[1]
            if repetitions - minima == 0: continue
            if repetitions - minima > 0: return 'NO'
        return 'YES'
    # general case
    chance = True
    for e in counter:
        repetitions = e[1]
        if repetitions - minima == 0: continue
        if repetitions - minima > 1: return 'NO'
        if chance and repetitions - minima == 1:
            chance = False
        else:
            return 'NO'
    return 'YES'

# test
# test = 'abcdefghhgfedecba'
# test = 'aabbccddeefghi'
test = 'abcdefghhgfedecba'
# test = 'aabbc'
print(f'testing with: {test}')
print(f'ans: {isValid(test)}')
