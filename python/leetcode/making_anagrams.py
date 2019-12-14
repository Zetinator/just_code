"""https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

Complete the makeAnagram function in the editor below. It must return an integer representing the minimum total characters that must be deleted to make the strings anagrams.
"""
from collections import Counter

def makeAnagram(str_a, str_b):
    c_a = Counter(str_a)
    c_b = Counter(str_b)
    diff = c_a - c_b
    diff += c_b - c_a
    # print(f'diff: {diff}, c_a: {c_a}, c_b: {c_b}')
    return sum(diff.values())

# test
a = 'cde'
b = 'abc'
print(f'testing with: a:{a}, b:{b}')
print(f'ans: {makeAnagram(a, b)}')

