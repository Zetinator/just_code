"""https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=search

Complete the function whatFlavors in the editor below. It must determine the two flavors they will purchase and print them as two space-separated integers on a line.

whatFlavors has the following parameter(s):

cost: an array of integers representing price for a flavor
money: an integer representing the amount of money they have to spend
"""

def whatFlavors(cost, money):
    """like in the video from google...
    https://www.youtube.com/watch?v=XKu_SEDAykw
    """
    complements = {}
    for i,e in enumerate(cost):
        if e in complements: return print(complements[e]+1, i+1)
        complement = money - e
        complements[complement] = i
    return

# test
money = 4
cost = [1, 4, 5, 3, 2]
print(f'testing with: {cost}')
print(f'ans: {whatFlavors(cost, money)}')
