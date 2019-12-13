"""https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_v%5B%5D=zen&h_v%5B%5D=zen&playlist_slugs%5B%5D%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D%5B%5D=arrays

It's New Year's Day and everyone's in line for the Wonderland rollercoaster ride! There are a number of people queued up, and each person wears a sticker indicating their initial position in the queue. Initial positions increment by 1 from 1 at the front of the line to n at the back.
"""

def minimumBribes(x):
    """find the number of bribes given or print 'Too chaotic' if state not posible'

    A person can bribe up to 2 times only
    """
    # special case: empty list
    if not x: return
    # general case
    bribes_given = 0
    # bubble sort?
    for i in reversed(range(len(x)-1)):
        local_swaps = 0
        while i < len(x)-1 and x[i] > x[i+1]:
            # swap
            x[i], x[i+1] = x[i+1], x[i]
            i += 1
            local_swaps += 1
            if local_swaps > 2: return 'Too chaotic'
        bribes_given += local_swaps
    return bribes_given

# test
test = [2, 1, 5, 3, 4]
# test = [2, 5, 1, 3, 4]
print(f'input: x: {test}')
print(f'ans: {minimumBribes(test)}')
