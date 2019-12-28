"""https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=linked-lists

Given a reference to the head of a doubly-linked list and an integer, , create a new DoublyLinkedListNode object having data value  and insert it into a sorted linked list while maintaining the sort.
"""
class DoublyLinkedListNode():
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def sortedInsert(head, data):
    # special case: empty list
    if not head or not data: return DoublyLinkedListNode(data)
    # special case: head > data
    if head.data > data:
        tmp = head
        head = DoublyLinkedListNode(data)
        head.next = tmp
        return head
    # general case
    current_node = head
    while current_node.next and current_node.next.data <= data:
        current_node = current_node.next
    tmp = current_node.next
    current_node.next = DoublyLinkedListNode(data)
    current_node.next.next = tmp
    return head

