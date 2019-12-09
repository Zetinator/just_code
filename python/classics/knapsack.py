"""knapsack... the classic
Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. It derives its name from the problem faced by someone who is constrained by a fixed-size knapsack and must fill it with the most valuable items.

https://en.wikipedia.org/wiki/Knapsack_problem
"""
from functools import lru_cache
from collections import namedtuple

@lru_cache(maxsize=1000)
def r(items, c_value, c_weight):
    # base case
    if not items: return c_value
    # special case: cannot take the item
    if c_weight - items[0].weight < 0: return r(items[1:], c_value, c_weight)
    # guess...
    return max(r(items[1:], c_value+items[0].value, c_weight-items[0].weight),  # take it
                r(items[1:], c_value, c_weight))  # or dont

def knapsack(items: list, max_weight: int) -> int:
    """find the max possible value of the items in the knapsack given the max_weight
    """
    return r(items, 0, max_weight)


# test
values = (60,100,120,10,150, 30)
weights = (10,20,30,50,200,5,60)
max_weight = 50
Item = namedtuple('Item', ['value', 'weight'])
items = tuple([Item(v, w) for v,w in zip(values, weights)])
print(f'testing with: items:{items}, max_weight:{max_weight}')
print(f'max value: {knapsack(items, max_weight)}')
