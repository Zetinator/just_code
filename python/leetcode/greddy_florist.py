"""https://www.hackerrank.com/challenges/greedy-florist/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=greedy-algorithms

Complete the getMinimumCost function in the editor below. It should return the minimum cost to purchase all of the flowers.

getMinimumCost has the following parameter(s):

c: an array of integers representing the original price of each flower
k: an integer, the number of friends
"""

def getMinimumCost(friends, flowers):
    s_flowers = sorted(flowers, key= lambda x: -x)
    minima, factor = 0, 1
    print(s_flowers)
    for i in range(0, len(s_flowers), friends):
        for e in s_flowers[i:i+friends]:
            print(f'subs: {s_flowers[i:i+friends]}, factor: {factor}, minima:{minima}')
            minima += e*factor
        factor += 1
    return minima

# test
friends = 3
flowers = [1, 3, 5, 7, 9]
print(f'testing with: {flowers}')
print(f'ans: {getMinimumCost(friends, flowers)}')
