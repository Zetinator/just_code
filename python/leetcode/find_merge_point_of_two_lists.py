"""https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=linked-lists

Given pointers to the head nodes of  linked lists that merge together at some point, find the Node where the two lists merge. It is guaranteed that the two head Nodes will be different, and neither will be NULL.
"""

def findMergeNode(head1, head2):
    """the original hash function of the class node
    uses the id of the object... so we just test membership
    """
    s_l = set()
    current_node = head1
    while current_node:
        s_l.add(current_node)
        current_node = current_node.next
    current_node = head2
    while current_node:
        if current_node in s_l: return current_node.data
        current_node = current_node.next
    return -1

