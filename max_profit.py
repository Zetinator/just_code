"""
You are given an array of integers representing the prices of a single stock on various days (each index in the array represents a different day). You are also given an integer k, which represents the number of transactions you are allowed to make. One transaction consists of buying the stock on a given day and selling it on another, later day. Write a function that returns the maximum profit that you can make buying and selling the stock, given k transactions. Note that you can only hold 1 share of the stock at a time; in other words, you cannot buy more than 1 share of the stock on any given day, and you cannot buy a share of the stock if you are still holding another share.
Sample input: [5, 11, 3, 50, 60, 90], 2
Sample output: 93 (Buy: 5, Sell: 11; Buy: 3, Sell: 90)
"""

def max_profit(x: 'Price of the stocks per day',
               k: 'Number of transactions availible') -> 'max profit':
    def try_stock_deep(x, stock, profit, k):
        print(f'STATUS: x:{x}, stock:{stock}, profit:{profit}, k:{k}')
        # reject
        if not k: return profit
        if not x: return profit
        # decisions... decisions
        if stock:
            return max(try_stock_deep(x[1:], None, profit+(x[0]-stock), k-1),  # we sell
                       try_stock_deep(x[1:], stock, profit, k))  # but what if we dont...
        else:
            return max(try_stock_deep(x[1:], x[0], profit, k),  # take a stock
                       try_stock_deep(x[1:], None, profit, k))  # what if we dont?
    return try_stock_deep(x, None, 0, k)

# test
x = [5, 11, 3, 50, 60, 90]
k = 2
print(f'testing with x:{x}, k:{k}')
print(f'ANS: {max_profit(x, k)}')
