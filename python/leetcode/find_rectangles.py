"""
We are given a N*M grid, print the number of rectangles in it.
"""
def find_rectangles(N: 'first dimension of the grip', 
                    M: 'second dimanesion of the grid') -> 'number of rectangles that can be fit':
    ans = 0
    for i in range(N):
        for f in range(M):
            rectangles = (N - i) * (M - f)
            ans += rectangles
            print(f'Rectangles found with window: {i+1}x{f+1}, --> {rectangles}')
    return ans

# test
N = 4
M = 3
print(f'testing with N:{N}, M:{M}')
print(f'ANS: {find_rectangles(N,M)}')



