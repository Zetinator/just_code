"""https://www.hackerrank.com/challenges/reverse-shuffle-merge/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=greedy-algorithms

Complete the reverseShuffleMerge function in the editor below. It must return the lexicographically smallest string fitting the criteria.

reverseShuffleMerge has the following parameter(s):

s: a string
"""
from collections import Counter

# Complete the reverseShuffleMerge function below.
def reverseShuffleMerge(s):
    freq = Counter(s)
    remain = Counter(s)
    used = Counter()
    res = []
    def can_pop(char):
        # are there still enough letter to make the word we want?
        needed_chars = freq[char]//2
        return used[char] + remain[char] - 1 >= needed_chars
    for letter in reversed(s):
        # we go backwards for that is our biggest clue
        # print(f'res: {res}, current_letter: {letter}')
        if freq[letter]//2 - used[letter] > 0:
            # backtracking-like, should we not use the letter?
            while res and res[-1] > letter and can_pop(res[-1]):
                removed_letter = res.pop()
                used[removed_letter] -= 1
            # general case: we use the letter
            used[letter] += 1
            res.append(letter)
        # update remaining letters
        remain[letter] -= 1
    return "".join(res)

# test
test = 'abcdefgabcdefg'
print(f'testing with: {test}')
print(f'ans: {reverseShuffleMerge(test)}')

