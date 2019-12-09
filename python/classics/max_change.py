"""
Coin Change problem: Given a list of coin values in a1, what is the minimum number of coins needed to get the value v?
"""
from functools import lru_cache

@lru_cache(maxsize=1000)
def r(x, coins, coins_used):
    """recursive implementation
    """
    if x <=0: return coins_used
    return min(r(x-coin, coins, coins_used+1) for coin in coins)

def max_change(money: int, coins: tuple) -> int:
    """finds the minimum combination of 'coins' to reach the 'money' quantity
    """
    return r(money, coins, 0)

# test
money = 24
coins = (1,3,4,5)
print(f'test with: money: {money}, coins: {coins}')
print(f'min coins: {max_change(money, coins)}')
