"""https://www.hackerrank.com/challenges/down-to-zero-ii/problem
"""

# the constrain is 0 <= N < 10**6
N = 10**6
moves = [0] + N * [N]
def downToZero(n):
    for i in range(N):
        # precompute all cases
        moves[i+1] = min(moves[i+1], moves[i] + 1)
        j = 2
        while j <= i and j * i <= N:
            moves[i*j] = min(moves[i*j], moves[i] + 1)
            j += 1

