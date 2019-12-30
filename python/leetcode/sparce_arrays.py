"""https://www.hackerrank.com/challenges/sparse-arrays/problem

There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings.
"""

from collections import Counter
def matchingStrings(strings, queries):
    counter = Counter()
    for word in strings:
        counter[word] += 1
    return [counter[q] for q in queries]

