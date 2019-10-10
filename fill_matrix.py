"""
Input: n = 2
Output: null
Explanation: We need to fill [1, 2, 3, 4] into a 2x2 matrix, which is not possible so return null.
"""
def fill_matrix(n: 'matrix NxN dimensions') -> 'matrix filled':
    numbers = [e for e in range(1, n**2+1)]  # those are rockie numbers
    def go_deep(numbers, n, ans):
        # reject
        if len(ans) > n:  # row by row
            temptation = sum(ans[:n])
            for i in range(1,len(ans)//n):
                if sum(ans[n*i:n*(i+1)]) != temptation: return None
        if len(ans) > (n**2 - n):  # column by column
            for i in range(n - len(numbers)):
                sum_column = 0
                for j in range(n):
                    sum_column += ans[j*n + i]
                if sum_column != temptation: return None
        if len(ans) == n**2: # diagonal by diagonal
            diagonal = 0
            a_diagonal = 0
            for i in range(n):
                diagonal += ans[i*n+i]
                a_diagonal += ans[i*n+(n-(i+1))]
            if diagonal != temptation or a_diagonal != temptation: return None
            print('...SUCCESS')

        # long live the kings
        if not numbers: return ans  # we are done
        # search and destroy
        print(f'STATUS: ans:{ans}')
        for i in range(len(numbers)):
            r = go_deep(numbers[:i]+numbers[i+1:], n, ans+[numbers[i]])
            if r: return r
        return None
    return go_deep(numbers, n, [])

# test
n = 4
print(f'testing with: {n}')
print(f'ANS: {fill_matrix(n)}')
