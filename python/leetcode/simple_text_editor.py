"""https://www.hackerrank.com/challenges/simple-text-editor/problem
In this challenge, you must implement a simple text editor. Initially, your editor contains an empty string, . You must perform  operations of the following  types:

append - Append string  to the end of .
delete - Delete the last  characters of .
print - Print the  character of .
undo - Undo the last (not previously undone) operation of type  or , reverting  to the state it was in prior to that operation.
"""

class TE():
    def __init__(self):
        self.stack = ['']
    def append(self, x):
        """append new string to the past string
        """
        if not x: return
        self.stack.append(self.stack[-1] + x)
    def delete(self, k):
        """delete the last k elements
        """
        self.stack.append(self.stack[-1][:-k])
    def print(self, k):
        """print the last k element
        """
        k -= 1
        print(self.stack[-1][k])
    def undo(self):
        """undo the last operation
        """
        self.stack.pop()

def execute_query(te, q):
    """simple interface to process the queries
    """
    if q[0] == '1':
        return te.append(q[1])
    if q[0] == '2':
        return te.delete(int(q[1]))
    if q[0] == '3':
        return te.print(int(q[1]))
    else: return te.undo()

# read from stdin
te = TE()
for _ in range(int(input())):
    q = [e for e in input().split()]
    execute_query(te, q)

# local test...
test = """1 abc
3 3
2 3
1 xy
3 2
4 
4 
3 1"""
_t = []
for line in test.split('\n'):
    tmp = []
    for e in line.split():
        tmp.append(e)
    _t.append(tmp)
test = _t
print(f'test with: {test}')
te = TE()
for q in test:
    execute_query(te, q)
