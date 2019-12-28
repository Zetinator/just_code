"""https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=linked-lists

You’re given the pointer to the head node of a doubly linked list. Reverse the order of the nodes in the list. The head node might be NULL to indicate that the list is empty. Change the next and prev pointers of all the nodes so that the direction of the list is reversed. Return a reference to the head node of the reversed list.
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
    print('')

def reverse(head):
    def r(current_node, parent):
        if not current_node:
            return parent
        sentinel = current_node.next
        current_node.next = parent
        return r(sentinel, current_node)
    return r(head, None)

# test
head = SinglyLinkedListNode(0)
head.next = SinglyLinkedListNode(1)
head.next.next = SinglyLinkedListNode(2)
head.next.next.next = SinglyLinkedListNode(3)
print(f'reverse:')
traverse(head)
head = reverse(head)
traverse(head)

