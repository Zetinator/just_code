"""
Given two strings ‘X’ and ‘Y’, find the length of the longest common substring.

Input : X = “GeeksforGeeks”, y = “GeeksQuiz”
Output : 5
The longest common substring is “Geeks” and is of length 5.
"""
from functools import lru_cache


@lru_cache(maxsize=1000)
def deep(x, y, record=0):
    if not x or not y: return record
    # print(f'STATUs: x: {x}, y: {y}, record: {record}')
    if x[0] == y[0]:
        return max(record, deep(x[1:], y[1:], record+1))
    return max(record, deep(x, y[1:], 0), deep(x[1:], y, 0))

def lcs(x, y):
    if not x or not y: return 0
    return deep(x, y)

# test 
e = 'kim es super bonita'
m = 'erick es lo maximo'
print(f'testing with: {e}, {m}') 
print(f'ans: {lcs(e, m)}')
