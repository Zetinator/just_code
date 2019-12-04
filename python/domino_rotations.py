def domino_rotations(A,B):
    candidate = A[0]
    n = 0
    def backtracking(A, B, candidate, n):
        # debug
        print('dominos left: A{}, B{}, rotations: {}'.format(str(A), str(B), n))
        # base return
        if A == []: return n
        # base case, should we rotate?
        if A[0] != candidate:
            if B[0] != candidate: return -1
            n += 1
        # ah shit... here we go again...
        return backtracking(A[1:], B[1:], candidate, n)
    return backtracking(A,B, candidate, n)

# test
# A = [3,5,1,2,3]; B = [3,6,3,3,4]
A = [2,1,2,4,2,2]; B = [5,2,6,2,3,2]
print('testing with A: {}, and B: {}'.format(A, B))
print('MIN ROTATIONS: {}'.format(domino_rotations(A,B)))
