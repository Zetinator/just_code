"""https://www.hackerrank.com/challenges/kindergarten-adventures/problem

Meera teaches a class of  students, and every day in her classroom is an adventure. Today is drawing day!

The students are sitting around a round table, and they are numbered from  to  in the clockwise direction. This means that the students are numbered , and students  and  are sitting next to each other.

After letting the students draw for a certain period of time, Meera starts collecting their work to ensure she has time to review all the drawings before the end of the day. However, some of her students aren't finished drawing! Each student  needs  extra minutes to complete their drawing.
"""

from collections import Counter
def solve(t):
    """array approach O(N)
    compute the thresholds... when a studen will finish and when not
    then just compute the index of the max prefix sum
    """
    counter = Counter()
    for i,e in enumerate(t):
        if e == 0 or e == len(t): continue
        finished_at = (i+1)%len(t)
        unfinished_at = (i-(e-1) + len(t))%len(t)
        counter[finished_at] += 1
        counter[unfinished_at] -= 1
    res, maximum, acc = None, -float('inf'), 0
    for i in range(len(t)):
        acc += counter[i]
        if maximum < acc:
            maximum = acc
            res = i
    return res + 1

# test
test = """1 0 0"""
test = """0 1 2"""
test = [int(e) for e in test.split()]
print(f'ans: {solve(test)}')
