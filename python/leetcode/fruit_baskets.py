"""
In a row of trees, the i-th tree produces fruit with type tree[i].

You start at any tree of your choice, then repeatedly perform the following steps:
    - Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
    - Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?
"""
def fruit_baskets(x: 'array of trees of different fruits')-> 'maximum of fruit to grab':
    def go_deep(x, basket):
        if len(basket) < 2: return 0
        print(f'STATUS: x:{x}, basket:{basket}')
        n = 0
        for e in x:
            if e in basket:
                n += 1
            else:
                break
        return max(n, go_deep(x[1:],x[1:3]))
    return go_deep(x,x[:2])

# test
test = [3,3,3,1,2,1,1,2,3,3,4]
print(f'testing with x: {test}')
print(f'ANS: {fruit_baskets(test)}')

