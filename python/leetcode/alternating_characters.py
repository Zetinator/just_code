"""https://www.hackerrank.com/challenges/alternating-characters/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings&h_r=next-challenge&h_v=zen

Complete the alternatingCharacters function in the editor below. It must return an integer representing the minimum number of deletions to make the alternating string.
"""

def alternatingCharacters(s):
    deletions = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]: deletions += 1
    return deletions


# test
a = 'AAABBB'
print(f'testing with: a:{a}')
print(f'ans: {alternatingCharacters(a)}')
