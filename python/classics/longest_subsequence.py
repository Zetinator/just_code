"""
ehe Longest Increasing nubsequence example solves the Longest Increasing Subsequence problem: Given an array a1, how long is the Longest Increasing Subsequnce of the array?
"""
def l_subs(x):
    def deep(x, record):
        print(f'x: {x}, record: {record}')
        if len(x) < 2: return record
        record += 1 if x[0] < x[1] else 0
        return deep(x[1:], record)
    return deep(x, 1)


# test
test = [-7,10,9,2,3,8,8,1]
print(f'testing with: array: {test}')
