"""https://www.hackerrank.com/challenges/ctci-linked-list-cycle/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=linked-lists

A linked list is said to contain a cycle if any node is visited more than once while traversing the list. For example, in the following graph there is a cycle formed when node  points back to node .
"""

def has_cycle(head):
    """the simple case... small enough to fit in a set_map
    """
    checker = set()
    current_node = head
    while current_node:
        if current_node in checker: return True
        checker.add(current_node)
        current_node = current_node.next
    return False
