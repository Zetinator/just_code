def kompare(A,B):
    mins = []
    A = A.split(',')
    B = B.split(',')
    def go_deep(A, B, mins):
        if B == []: return mins
        def go_deeper(A, word, n):
            if A == []: return n
            if A[0].count(min(A[0])) < word.count(min(word)):
                return go_deeper(A[1:], word, n+1)
            else:
                return go_deeper(A[1:], word, n)
        mins.append(go_deeper(A, B[0], 0))
        return go_deep(A, B[1:], mins)
    return go_deep(A, B, mins)

# testing
A = 'abcd,aabc,bd'
B = 'aaa,aa'

print('testing with A:{} vs B:{}'.format(A,B))
print(str(kompare(A,B)))
