"""https://www.hackerrank.com/challenges/mark-and-toys/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=sorting&h_r=next-challenge&h_v=zen
Mark and Jane are very happy after having their first child. Their son loves toys, so Mark wants to buy some. There are a number of different toys lying in front of him, tagged with their prices. Mark has only a certain amount to spend, and he wants to maximize the number of toys he buys with this money.
"""

# dynamic programming
def maximumToys(prices, k):
    def r(prices, money_left, max_toys):
        if not prices: return max_toys
        if money_left - prices[0] < 0: return r(prices[1:], money_left, max_toys)
        return max(r(prices[1:], money_left-prices[0], max_toys+1),  # what if you take it...
                    r(prices[1:], money_left, max_toys))  # what if you dont...
    return r(prices, k, 0)


# avoid the stack overflow from hackerrank
def maximumToys(prices, k):
    prices.sort()
    for i, _ in enumerate(prices):
        k -= prices[i]
        if k <= 0: return i
    return i


# test
prices = [1, 12, 5, 111, 200, 1000, 10]
money_left = 50
print(f'testing with: prices: {prices}, money: {money_left}')
print(f'ans: {maximumToys(prices, money_left)}')
