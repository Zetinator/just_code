"""https://www.hackerrank.com/challenges/min-max-riddle/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=stacks-queues

Complete the riddle function in the editor below. It must return an array of integers representing the maximum minimum value for each window size from  to .

riddle has the following parameter(s):

arr: an array of integers
"""

def riddle(arr):
    """similar to the largest rectangle...
    """
    stack = []
    windows = {}
    # to pop all the remaining elements in the stack
    tmp = arr[:]
    tmp.append(-float('inf'))
    # we get how big is the window for which this item is min
    for i in range(len(tmp)):
        indexed = i
        while stack and tmp[i] <= stack[-1][0]:
            n, indexed = stack.pop()
            window = i - indexed
            windows[n] = window
        stack.append((tmp[i], indexed))
    # we get the max's per window size
    maxs = sorted((k,v) for k,v in windows.items())
    max_windows = {v:k for k,v in maxs}
    current = max_windows.get(len(arr), None)
    res = []
    for i in reversed(range(len(arr))):
        current = max_windows.get(i+1, current)
        res.append(current)
    # don forget to remove the extra -float('inf')
    res.reverse()
    return res

def riddle(arr):
    windows, stack, curr = {}, [], 0
    arr.append(-float('inf'))
    for i,e in enumerate(arr):
        while stack and arr[stack[-1]] >= e:
            val = arr[stack.pop()]
            l = i - (stack and stack[-1] + 1 or 0)
            windows[l] = max(windows.get(l,-float('inf')), val)
        stack.append(i)
    ans = [0] * (len(arr) - 1)
    for k in range(len(arr) - 1, 0, -1):
        curr = max(curr, windows.get(k, curr))
        ans[k-1] = curr
    return ans

def riddle(arr):
    """similar to the largest rectangle...
    """
    stack = []
    windows = {}
    # to pop all the remaining elements in the stack
    tmp = arr[:] + [-float('inf')]
    # we get how big is the window for which this item is min
    for i in range(len(tmp)):
        indexed = i
        while stack and tmp[i] <= stack[-1][0]:
            n, indexed = stack.pop()
            window = i - indexed
            windows[window] = max(windows.get(window,0), n)
        stack.append((tmp[i], indexed))
    # we get the max's per window size
    res, current = [0]*len(arr), 0
    for i in reversed(range(len(arr))):
        current = max(windows.get(i+1, current), current)
        res[i] = current
    return res


test = [2,6,1,12]
test = [11, 2, 3, 14, 5, 2, 11, 12]
print(f'testing with: {test}')
print(f'ans: {riddle(test)}')
