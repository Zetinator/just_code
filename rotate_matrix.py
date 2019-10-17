"""
Given an square matrix, turn it by 90 degrees in anti-clockwise direction without using any extra space.
Input
 1  2  3
 4  5  6
 7  8  9

Output:
 3  6  9 
 2  5  8 
 1  4  7 
 """
def rotate_aclockwise(x: 'matrix NxN') -> 'matrix NxN':
    n = len(x)
    y = [[None]*len(x) for i in x]
    for i in range(n):
        for j in range(n):
            y[j][i] = x[i][(n-1) - j]
    for e in y: print(e)
    return y

def rotate_inplace(x: 'matrix NxN') -> 'matrix NxN':
    n = len(x)
    layers = n//2
    for layer in range(layers):
        for e in range((n-1) - layer*2):
            # get swapy
            x[layer][layer+e], x[layer+e][(n-1)-layer] = (x[layer+e][(n-1)-layer], 
                                                                x[layer][layer + e])
            x[layer+e][(n-1)-layer], x[(n-1)-layer][(n-1)-(layer+e)] = (x[(n-1)-layer][(n-1)-(layer+e)],
                                                                       x[layer+e][(n-1)-layer])
            x[(n-1)-layer][(n-1)-(layer+e)], x[(n-1)-(layer+e)][layer] = (x[(n-1) - (layer + e)][layer],
                                                                         x[(n-1)-layer][(n-1)-(layer+e)])
    return x

# test
print('testing with:')
test = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]
for e in test:
    print(e)
print('ANS:')
for e in rotate_inplace(test):
    print(e)
