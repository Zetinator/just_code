"""
You are given 2 arrays representing integer locations of stores and houses (each location in this problem is one-dementional). For each house, find the store closest to it.
Return an integer array result where result[i] should denote the location of the store closest to the i-th house. If many stores are equidistant from a particular house, choose the store with the smallest numerical location. Note that there may be multiple stores and houses at the same location.
Input: houses = [5, 10, 17], stores = [1, 5, 20, 11, 16]
Output: [5, 11, 16]
Explanation:
The closest store to the house at location 5 is the store at the same location.
The closest store to the house at location 10 is the store at the location 11.
The closest store to the house at location 17 is the store at the location 16.
"""
def stores_houses(x: 'array with houses', y: 'array with stores') -> 'array with the closest store':
    def go_deep(x, y, ans):
        print(f'STATUS: x:{x}, y:{y}, ans:{ans}')
        if not x: return ans
        min_store = sorted(y, key=lambda y: abs(y - x[0]))[0]
        return go_deep(x[1:], y, ans + [min_store])
    return go_deep(x, y, [])

# test
x = [5, 10, 17]
y = [1, 5, 20, 11, 16]
print(f'testing with: houses:{x}, stores:{y}')
print(f'ANS: {stores_houses(x, y)}')

