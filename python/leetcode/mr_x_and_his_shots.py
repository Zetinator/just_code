"""https://www.hackerrank.com/challenges/x-and-his-shots/problem

A cricket match is going to be held. The field is represented by a 1D plane. A cricketer, Mr. X has  favorite shots. Each shot has a particular range. The range of the  shot is from i to i. That means his favorite shot can be anywhere in this range. Each player on the opposite team can field only in a particular range. Player  can field from i to i. You are given the  favorite shots of Mr. X and the range of  players"""
def bs_left(value, arr):
    l, r = 0, len(arr)
    while l < r:
        m = (l+r)//2
        if arr[m] == value: return m
        if value < arr[m]:
            r = m
        else:
            l = m+1
    return l

def bs_right(value, arr):
    l, r = 0, len(arr)
    while l < r:
        m = (l+r)//2
        if arr[m] == value: return m+1
        if value < arr[m]:
            r = m
        else:
            l = m+1
    return l

from bisect import bisect_left, bisect_right

def solve(shots, players):
    """interval tree... or binary search...
    """
    start, end = [], []
    # separate starts and ends points...
    for shot in shots:
        i, j = shot
        start.append(i)
        end.append(j)
    # sort...
    start.sort()
    end.sort()
    res = 0
    # find with binary search how many intervals to consider...
    for player in players:
        i, j = player
        res += bisect_right(start, j) - bisect_left(end, i)
    return res

shots = """1 2
2 3
4 5
6 7"""
players = """1 5
2 3
4 7
5 7"""
_ = []

for line in shots.split('\n'):
    tmp = []
    for e in line.split():
        tmp.append(int(e))
    _.append(tmp)
shots = _
_ = []
for line in players.split('\n'):
    tmp = []
    for e in line.split():
        tmp.append(int(e))
    _.append(tmp)
players = _

print(f'testing with: arr: {shots}, players: {players}')
print(f'ans: {solve(shots, players)}')
