"""
The Coin Change example solves the Coin Change problem: Given a list of coin values in a1, what is the minimum number of coins needed to get the value v?
"""
def max_change(money, coins):
    def deep(x, coins, coins_used):
        print(f'STATUS: money_left: {x}, coins_used: {coins_used}')
        if x <=0: return coins_used
        return min(deep(x-coin, coins, coins_used+1) for coin in coins)
    return deep(money, coins, 0)

# test
money = 7
coins = [1,3,4,5]
print(f'test with: money: {money}, coins: {coins}')
print(f'min coins: {max_change(money, coins)}')
