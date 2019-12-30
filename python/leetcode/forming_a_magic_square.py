"""https://www.hackerrank.com/challenges/magic-square-forming/problem

We define a magic square to be an  matrix of distinct positive integers from  to  where the sum of any row, column, or diagonal of length  is always equal to the same number: the magic constant.
"""
def reject(s):
    n = len(s)
    magic_constant = n*(n**2+1)//2
    diagonal = []
    a_diagonal = []
    antidiagonal = []
    for i, line in enumerate(s):
        column = []
        if sum(line) != magic_constant: return True
        for j, e in enumerate(line):
            if i == j: diagonal.append(s[i][j])
            if (n-1-i) == j: a_diagonal.append(s[i][j])
            column.append(s[j][i])
        if sum(column) != magic_constant: return True
    if sum(diagonal) != magic_constant: return True
    if sum(a_diagonal) != magic_constant: return True
    return


def formingMagicSquare(s):
    use = [n for n in range(10)]
    def backtrack(ss, node, use, acc):
        i, j = node
        # move square-wise
        if j%len(ss) == 0: i += 1
        # accept
        if i == len(ss) and not reject(ss):
            return acc
        # we use the clossest to the number present everytime... greddy
        use = sorted(use, key=lambda x: -abs(ss[i][j]-x))
        while use:
            n = use.pop()
            print(f'pos: {node}, try: {n}')
            delta, ss[i][j] = s[i][j] - n, n
            res = []
            res = backtrack(ss, (i,j), use, acc+delta)
            if res != None: return res
    return backtrack(s[:], (0,0), use, 0)

def formingMagicSquare(s):
    n = len(s)
    s = [e for line in s for e in line]
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
        numbers.sort(key=lambda x: -abs(s[len(ans)]-x))
        for i in range(len(numbers)):
            r = go_deep(numbers[:i]+numbers[i+1:], n, ans+[numbers[i]])
            if r: return r
        return None
    return go_deep(numbers, n, [])

# approach didnt work... trying precomputing all the posible 3x3 magic squares...
import sys
diffs = []
s = []
for s_i in range(3):
   s_t = [int(s_temp) for s_temp in input().strip().split(' ')]
   s.append(s_t)

all_possible = [
            [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]],]

#compare s to each in all possible get number of differences for each to diffs
for possiblity in all_possible:
    cost = 0
    for p_row, s_row in list(zip(possiblity,s)):
        for p_num, s_num in (list(zip(p_row, s_row))):
            if p_num != s_num:
                cost += abs(p_num - s_num)
    diffs.append(cost)
print(min(diffs))

test = """8 3 4
1 5 9
6 7 2"""

test = """4 9 2
3 5 7
8 1 5"""

_t= []
for line in test.split('\n'): 
    tmp = []
    for n in line.split(' '):
        tmp.append(int(n))
    _t.append(tmp)
test = _t
print(test)
print(f'ans: {formingMagicSquare(test)}')
