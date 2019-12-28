"""https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=linked-lists

You’re given the pointer to the head node of a linked list, an integer to add to the list and the position at which the integer must be inserted. Create a new node with the given integer, insert this node at the desired position and return the head node.

A position of 0 indicates head, a position of 1 indicates one node away from the head and so on. The head pointer given may be null meaning that the initial list is empty.
"""

class SinglyLinkedListNode():
    def __init__(self, data):
        self.data = data
        self.next = None

def traverse(head):
    if not head: return
    current_node = head
    while current_node:
        print(f'-->({current_node.data})', end='')
        current_node = current_node.next

def insertNodeAtPosition(head, data, position):
    # special case: empty list
    if not head: return SinglyLinkedListNode(data)
    # special case: index 0
    if position == 0:
        tmp = head
        head = SinglyLinkedListNode(data)
        head.next = tmp
        return head
    # general case...
    current_node = head
    while (position -1) and current_node.next:
        current_node = current_node.next
        position -= 1
    sentinel = current_node.next
    current_node.next = SinglyLinkedListNode(data)
    current_node.next.next = sentinel
    return head

# test
head = SinglyLinkedListNode(0)
head.next = SinglyLinkedListNode(1)
head.next.next = SinglyLinkedListNode(2)
head.next.next.next = SinglyLinkedListNode(3)
data, pos = 69, 2
head = insertNodeAtPosition(head, data, pos)
print(f'insert {data} in {pos}')
traverse(head)
