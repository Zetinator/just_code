"""
Given two strings, determine if they share a common substring. A substring may be as small as one character.

For example, the words "a", "and", "art" share the common substring . The words "be" and "cat" do not share a substring.
"""
def contains(x,y):
    x = set(x)
    ans = [e in x for e in y]
    return any(ans)

# test
x = 'hi'
y = 'world'
print(f'x: {x}')
print(f'y: {y}')
print(f'ans: {contains(x,y)}')
