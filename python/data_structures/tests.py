import unittest
from bst import BST
from avl import AVL
from max_heap import Heap
from segment_tree import ST
from linked_list import LinkedList
from double_linked_list import DoubleLinkedList
from queue import Queue
from stack import Stack

class TestDataStructures(unittest.TestCase):

    def test_avl(self):
        test = [33, 66, 1, 65, 5, 7, 41, 74, 11, 45, 14, 60, 48, 84, 85, 31, 93, 63]
        avl = AVL(test)
        self.assertEqual(avl.search(93).data, 93)

    def test_bst(self):
        test = [33, 66, 1, 65, 5, 7, 41, 74, 11, 45, 14, 60, 48, 84, 85, 31, 93, 63]
        bst = BST(test)
        self.assertEqual(bst.search(93).data, 93)

    def test_heap(self):
        test = [33, 66, 1, 65, 5, 7, 41, 74, 11, 45, 14, 60, 48, 84, 85, 31, 93, 63]
        heap = Heap(test)
        self.assertEqual(heap.pop(), 93)

    def test_segment_tree(self):
        test = [33, 66, 1, 65, 5, 7, 41, 74, 11, 45, 14, 60, 48, 84, 85, 31, 93, 63]
        st = ST(test)
        self.assertEqual(st.query(0,2), 66)

    def test_linked_list(self):
        ll = LinkedList(range(10))
        self.assertEqual(ll.head.data, 0)

    def test_double_linked_list(self):
        dll = DoubleLinkedList(range(10))
        self.assertEqual(dll.head.data, 0)
 
    def test_queue(self):
        q = Queue(range(10))
        self.assertEqual(q.pop().data, 0)

    def test_stack(self):
        s = Stack(range(10))
        self.assertEqual(s.pop().data, 9)

if __name__ == '__main__':
    unittest.main()
