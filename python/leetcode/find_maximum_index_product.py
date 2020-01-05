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
    """we keep a stack to access the next biggest in O(1)
    """
    stack_left, stack_right = [], []
    left, right = [], []
    # left -> right
    for i,e in enumerate(arr):
        while stack_left and e >= stack_left[-1][0]:
            stack_left.pop()
        left.append(stack_left[-1][1] if stack_left else 0)
        stack_left.append((e, i+1))
    # right -> left
    for i in reversed(range(len(arr))):
        while stack_right and arr[i] >= stack_right[-1][0]:
            stack_right.pop()
        right.append(stack_right[-1][1] if stack_right else 0)
        stack_right.append((arr[i], i+1))
    # multiply and we are done...
    res = -float('inf')
    for i,e in enumerate(left):
        res = max(res, (left[i])*(right[len(right)-1 -i]))
    return res

test = """5 4 3 4 5"""
test = [int(e) for e in test.split()]
with open('./test_data.txt', 'r') as f:
    for line in f:
        test = [int(n) for n in line.split()]
print(f'testing with: {test[:10]}...')
print(f'ans: {solve(test)}')
