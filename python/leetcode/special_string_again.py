"""https://www.hackerrank.com/challenges/special-palindrome-again/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=strings

A string is said to be a special string if either of two conditions is met:

All of the characters are the same, e.g. aaa.
All characters except the middle one are the same, e.g. aadaa.
A special substring is any substring of a string which meets one of those criteria. Given a string, determine how many special substrings can be formed from it.
"""

def is_special(s):
    """checks if the substring is "special"
    """
    # special case:
    if len(s) == 1: return True
    # general case
    match = s[0]
    for i in range(len(s)//2):
        if s[i] != match or s[i] != s[-(1+i)]: return False
    return True

def substrCount(n, s):
    """counts how many substrings are "special"

    somehow not fast enought... maybe because of the function call
    """
    n_specials = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            n_specials += 1 if is_special(s[i:j+1]) else 0
    return n_specials

def substrCount(n, s):
    res = 0
    count_sequence = 0
    prev = ''
    for i,v in enumerate(s):
        # first increase counter for all seperate characters
        count_sequence += 1
        if i and (prev != v):
            # if this is not the first char in the string
            # and it is not same as previous char,
            # we should check for sequence x.x, xx.xx, xxx.xxx etc
            # and we know it cant be longer on the right side than
            # the sequence we already found on the left side.
            j = 1
            while ((i-j) >= 0) and ((i+j) < len(s)) and j <= count_sequence:
                # make sure the chars to the right and left are equal
                # to the char in the previous found squence
                if s[i-j] == prev == s[i+j]:
                    # if so increase total score and step one step further out
                    res += 1
                    j += 1
                else:
                    # no need to loop any further if this loop did
                    # not find an x.x  pattern
                    break
            #if the current char is different from previous, reset counter to 1
            count_sequence = 1
        res += count_sequence
        prev = v
    return res

# test
# s = 'asasd'
s = 'abcbaba'
n = 5
print(f'testing with: {s}')
print(f'ans: {substrCount(n, s)}')
