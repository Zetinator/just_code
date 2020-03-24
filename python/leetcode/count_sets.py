def count_sets(arr: list, total: int)-> list:
    count_sets.states = []
    def dp(sub, total, current=[]):
        if not sub:
            if int(sum(current)) == total:
                count_sets.states.append(current)
            return
        dp(sub[1:], total, current+sub[:1])  # we take it
        dp(sub[1:], total, current)  # we dont
    dp(arr, total)
    return count_sets.states

test = [2,4,6,10]
total = 16
print(f'number of sets that sum to {total} in {test} is: {count_sets(test, total)}')
