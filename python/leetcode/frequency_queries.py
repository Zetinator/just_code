"""https://www.hackerrank.com/challenges/frequency-queries/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

You are given  queries. Each query is of the form two integers described below:
-  1x: Insert x in your data structure.
-  2y: Delete one occurence of y from your data structure, if present.
-  3z: Check if any integer is present whose frequency is exactly . If yes, print 1 else 0.
"""
from collections import Counter

def freqQuery(queries):
    """execute the given queries
    we need one counter to relate element -> frequency (counter)
    and another counter to relate frequency -> elements (freq_counter)
    this last one is updated everytime the frequency of an element changes...
    """
    counter = Counter()
    freq_counter = Counter()
    res = []
    for q in queries:
        instruction, value = q
        if instruction == 1:
            # standard insert
            freq_counter[counter[value]] -= 1
            counter[value] += 1
            freq_counter[counter[value]] += 1
        elif instruction == 2:
            # we need to skip the negative counters... they were causing an error
            if freq_counter[counter[value]] <= 0: continue
            freq_counter[counter[value]] -= 1
            counter[value] -= 1
            freq_counter[counter[value]] += 1
        else:
            res.append(1 if freq_counter[value] > 0 else 0)
    return res

# test
test = [[3, 4],
        [2, 1003],
        [1, 16],
        [3, 1]]
print('testing with:')
for line in test: print(line)
print(f'ans: {freqQuery(test)}')
