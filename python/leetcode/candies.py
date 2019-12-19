"""https://www.hackerrank.com/challenges/candies/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=dynamic-programming

Alice is a kindergarten teacher. She wants to give some candies to the children in her class.  All the children sit in a line and each of them has a rating score according to his or her performance in the class.  Alice wants to give at least 1 candy to each child. If two children sit next to each other, then the one with the higher rating must get more candies. Alice wants to minimize the total number of candies she must buy.

For example, assume her students' ratings are [4, 6, 4, 5, 6, 2]. She gives the students candy in the following minimal amounts: [1, 2, 1, 2, 3, 1]. She must buy a minimum of 10 candies.
"""
import time

def candies(n, arr):
    """dev version
    returns score with traceback
    """
    def r(arr, prev, acc, ans=None):
        # remember...
        time.sleep(.1)
        p_grade, p_candie = prev
        if not arr: return (acc, (p_grade,p_candie))
        c_candie = 1
        while True:
            print(f'arr: {arr}, c: {arr[0]}, p_candie: {p_candie}')
            # depending on the past state decide
            if arr[0] <= p_grade:
                if p_candie - 1 <= 0: print('geht nicht...'); return
                ans = r(arr[1:], (arr[0], c_candie), acc + c_candie)
            if arr[0] > p_grade:
                ans =  r(arr[1:], (arr[0], p_candie+1), acc + p_candie+1)
            # if failure... change current_state
            if ans:
                return ans + ((p_grade,p_candie),)
            else:
                c_candie += 1
    retry = 1
    while True:
        ans = r(arr[1:], (arr[0], retry), retry)
        if ans:
            score, *traceback = ans
            traceback.reverse()
            print(f'traceback: {traceback}')
            return score
        retry += 1

from functools import lru_cache
import sys
sys.setrecursionlimit(100000)

def candies(n, arr):
    """prod version
    some good old backtracking...
    """
    candies = [1] * len(arr)
    def r(i):
        # accept
        if i == len(arr): return True
        if i < len(arr)-1 and arr[i] < arr[i+1]:
            candies[i+1] = candies[i] + 1
            return r(i+1)
        # reject
        if arr[i-1] > arr[i] and candies[i-1] - 1 == 0:
            return
        # change state
        while True:
            if r(i+1): return True
            candies[i] += 1
    # init
    while True:
        if r(0):
            return sum(candies)
        else:
            candies[0] += 1

def candies(n, arr):
    """naive approach
    """
    candies = [1] * len(arr)
    # left -> right
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            candies[i+1] = max(candies[i+1], candies[i] + 1)
    # right -> left
    for i in reversed(range(1, len(arr))):
        if arr[i] < arr[i-1]:
            candies[i-1] = max(candies[i-1], candies[i] + 1)
    return sum(candies)



test = [4, 6, 4, 5, 6, 2]
test = [1,2,2]
# test = [2,4,2,6,1,7,8,9,2,1]
# test = [2,4,3,5,2,6,4,5]
n = len(test)
print(f'testing with: {test}')
print(f'ans: {candies(n, test)}')

