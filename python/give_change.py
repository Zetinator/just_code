def give_change(quantity):
    coins = [25, 10, 5, 1]
    def go_deep(quantity, coins, change):
        print('STATUS: quantity: {}, coins:{}, change:{}'.format(quantity, coins, change))
        if quantity <= 0: return change
        n = quantity // coins[0]
        change[coins[0]] = n
        quantity -= n*coins[0]
        return go_deep(quantity, coins[1:], change)
    return go_deep(quantity, coins, {})

# test
print('testing with 2350')
print(give_change(2399))
