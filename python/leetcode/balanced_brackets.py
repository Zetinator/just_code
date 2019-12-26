"""https://www.hackerrank.com/challenges/balanced-brackets/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues

By this logic, we say a sequence of brackets is balanced if the following conditions are met:

It contains no unmatched brackets.
The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets.
Given  strings of brackets, determine whether each sequence of brackets is balanced. If a string is balanced, return YES. Otherwise, return NO.
"""

def isBalanced(s):
    opening = {'{','[','('}
    closing = {'}':'{',']':'[',')':'('}
    brackets = []
    for e in s:
        if e in opening:
            brackets.append(e)
        if e in closing:
            if not brackets or closing[e] != brackets.pop():
                return 'NO'
    # only if the stack if empty is balanced
    return 'YES' if not brackets else 'NO'


test = '{[(])}'
test = '{{[[(())]]}}'
print(f'testing with: {test}')
print(f'ans: {isBalanced(test)}')
