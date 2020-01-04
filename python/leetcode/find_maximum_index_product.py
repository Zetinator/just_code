"""https://www.hackerrank.com/challenges/find-maximum-index-product/problem

You are given a list of  numbers . For each element at position  (), we define  and  as:
Sample Input
5
5 4 3 4 5
Sample Output
8
Explanation
We can compute the following:
The largest of these is 8, so it is the answer.
"""
def solve(arr):
    stack_left, stack_right = [(arr[0], 0)], [(arr[-1], len(arr)-1)]
    left, right = [0], [0]
    # left -> right
    for i,e in enumerate(arr[1:], 1):
        while stack_left and e >= stack_left[-1][0]:
            stack_left.pop()
        left.append(stack_left[-1][1] if stack_left else 0)
        stack_left.append((e, i))
    # right -> left
    for i in reversed(range(len(arr)-1)):
        while stack_right and arr[i] >= stack_right[-1][0]:
            stack_right.pop()
        right.append(stack_right[-1][1] if stack_right else 0)
        stack_right.append((arr[i], i))
    print(f'len: {len(left)}, left: {left[49995:50003]}')
    print(f'len: {len(right)}, right: {right[49995:50003]}')
    # multiply and we are done...
    res = -float('inf')
    for i,e in enumerate(left):
        res = max(res, (left[i]+1)*(right[i]+1))
    return res

test = """5 4 3 4 5"""
test = [int(e) for e in test.split()]
with open('./test_data.txt', 'r') as f:
    for line in f:
        test = [int(n) for n in line.split()]
print(f'testing with: {test[:10]}...')
print(f'ans: {solve(test)}')
