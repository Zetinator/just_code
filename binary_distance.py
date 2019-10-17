"""
The distance between 2 binary strings is the sum of their lengths after removing the common prefix. For example: the common prefix of 1011000 and 1011110 is 1011 so the distance is len("000") + len("110") = 3 + 3 = 6.

Given a list of binary strings, pick a pair that gives you maximum distance among all possible pair and return that distance.
"""
def binary_distance(x: 'binary string', y: 'binary string') -> 'distance':
    def find_prefix(x, y, n):
        if not x or not y: return n
        # print(f'STATUS: x:{x}, y:{y}, n:{n}')
        if x[0] == y[0]:
            return find_prefix(x[1:], y[1:], n+1)
        else:
            return n
    prefix_len = find_prefix(x, y, 0)
    x, y = x[prefix_len:], y[prefix_len:]
    return len(x) + len(y)

# test
x = '1011000'
y = '1011110'
print(f'testing with: x:{x}, y:{y}')
print(f'ANS: {binary_distance(x, y)}')

