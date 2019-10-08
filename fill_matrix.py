"""
Input: n = 2
Output: null
Explanation: We need to fill [1, 2, 3, 4] into a 2x2 matrix, which is not possible so return null.
"""
def check_magic(x: 'flat matrix', n: 'NxN'):
    print(f'CHECKING: {x}', end='\r')
    magic = sum(x[:n])
    diagonal = 0
    a_diagonal = 0
    for i in range(n):
        if sum(x[i*n:(i+1)*n]) != magic: return False
        diagonal += x[i*n+i]
        a_diagonal += x[i*n+(n-(i+1))]
        sum_col = 0
        for j in range(n):
            sum_col += x[j*n+i]
        if sum_col != magic: return False
    if not diagonal == magic or not a_diagonal == magic: return False
    print('\n...SUCCESS')
    return True

def fill_matrix(n: 'matrix NxN dimensions') -> 'matrix filled':
    numbers = [e for e in range(1, n**2+1)]
    def go_deep(numbers, n, ans):
        if not numbers:
            if check_magic(ans, n):
                return ans
            else:
                return None
        # print(f'STATUS: numbers:{numbers}, ans:{ans}')
        for i in range(len(numbers)):
            r = go_deep(numbers[:i]+numbers[i+1:], n, ans+[numbers[i]])
            if r: return r
        return None
    return go_deep(numbers, n, [])

# test
n = 4
print(f'testing with: {n}')
print(f'ANS: {fill_matrix(n)}')
