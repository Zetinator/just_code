import unittest
from data_structures import *
from algorithms import *

class TestDataAlgorithms(unittest.TestCase):
    def test_binary_search(self):
        test = [3, 3, 11, 12, 13, 21, 23, 23, 25, 27, 29, 32, 35, 51, 59, 68, 73, 77, 92]
        self.assertEqual(bs(test, 11), 2)
    def test_bubble_sort(self):
        test = [51, 3, 35, 92, 11, 13, 29, 12, 68, 77, 59, 25, 73, 32, 23, 3, 27, 23, 21]
        ans = [3, 3, 11, 12, 13, 21, 23, 23, 25, 27, 29, 32, 35, 51, 59, 68, 73, 77, 92]
        self.assertEqual(bubble_sort(test), ans)
    def test_selection_sort(self):
        test = [51, 3, 35, 92, 11, 13, 29, 12, 68, 77, 59, 25, 73, 32, 23, 3, 27, 23, 21]
        ans = [3, 3, 11, 12, 13, 21, 23, 23, 25, 27, 29, 32, 35, 51, 59, 68, 73, 77, 92]
        self.assertEqual(selection_sort(test), ans)
    def test_insertion_sort(self):
        test = [51, 3, 35, 92, 11, 13, 29, 12, 68, 77, 59, 25, 73, 32, 23, 3, 27, 23, 21]
        ans = [3, 3, 11, 12, 13, 21, 23, 23, 25, 27, 29, 32, 35, 51, 59, 68, 73, 77, 92]
        self.assertEqual(insertion_sort(test), ans)
    def test_merge_sort(self):
        test = [51, 3, 35, 92, 11, 13, 29, 12, 68, 77, 59, 25, 73, 32, 23, 3, 27, 23, 21]
        ans = [3, 3, 11, 12, 13, 21, 23, 23, 25, 27, 29, 32, 35, 51, 59, 68, 73, 77, 92]
        self.assertEqual(merge_sort(test), ans)
    def test_quick_sort(self):
        test = [51, 3, 35, 92, 11, 13, 29, 12, 68, 77, 59, 25, 73, 32, 23, 3, 27, 23, 21]
        ans = [3, 3, 11, 12, 13, 21, 23, 23, 25, 27, 29, 32, 35, 51, 59, 68, 73, 77, 92]
        self.assertEqual(quick_sort(test), ans)
    def test_random_quick_sort(self):
        test = [51, 3, 35, 92, 11, 13, 29, 12, 68, 77, 59, 25, 73, 32, 23, 3, 27, 23, 21]
        ans = [3, 3, 11, 12, 13, 21, 23, 23, 25, 27, 29, 32, 35, 51, 59, 68, 73, 77, 92]
        self.assertEqual(r_quick_sort(test), ans)
    def test_heap_sort(self):
        test = [51, 3, 35, 92, 11, 13, 29, 12, 68, 77, 59, 25, 73, 32, 23, 3, 27, 23, 21]
        ans = [3, 3, 11, 12, 13, 21, 23, 23, 25, 27, 29, 32, 35, 51, 59, 68, 73, 77, 92]
        self.assertEqual(heap_sort(test), ans)
    def test_quick_select(self):
        test = [51, 3, 35, 92, 11, 13, 29, 12, 68, 77, 59, 25, 73, 32, 23, 3, 27, 23, 21]
        ans = [3, 3, 11, 12, 13, 21, 23, 23, 25, 27, 29, 32, 35, 51, 59, 68, 73, 77, 92]
        self.assertEqual(quick_select(test, 8), 27)
    def test_boyer_moore(self):
        pattern = 'marion'
        text = "erick quiere a marion, aunque marion ya no nos hable :("
        self.assertEqual(boyer_moore(pattern, text), 15)
    def test_dfs(self):
        g = { "a" : ["c"],
                  "b" : ["c", "e"],
                  "c" : ["a", "b", "d", "e"],
                  "d" : ["c"],
                  "e" : ["c", "b"],
                  "f" : []
                }
        g = graph.Graph(g)
        self.assertEqual(dfs(g, 'a', 'b'), ['a', 'c', 'b'])

class TestDataStructures(unittest.TestCase):
    def test_avl(self):
        test = [33, 66, 1, 65, 5, 7, 41, 74, 11, 45, 14, 60, 48, 84, 85, 31, 93, 63]
        avl = AVL(test)
        self.assertEqual(avl.search(93).value, 93)

    def test_bst(self):
        test = [33, 66, 1, 65, 5, 7, 41, 74, 11, 45, 14, 60, 48, 84, 85, 31, 93, 63]
        bst = BST(test)
        self.assertEqual(bst.search(93).value, 93)

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
        self.assertEqual(ll.head.value, 0)

    def test_double_linked_list(self):
        dll = DoubleLinkedList(range(10))
        self.assertEqual(dll.head.value, 0)
 
    def test_queue(self):
        q = Queue(range(10))
        self.assertEqual(q.pop().value, 0)

    def test_stack(self):
        s = Stack(range(10))
        self.assertEqual(s.pop().value, 9)

    def test_trie(self):
        keys  = 'erick quiere mucho a su marion aunque ella ya no nos quiera tanto'.split()
        trie = Trie(keys)
        self.assertEqual(trie.search('marion'), 'marion')

    def test_graph(self):
        graph = { "a" : ["c"],
                  "b" : ["c", "e"],
                  "c" : ["a", "b", "d", "e"],
                  "d" : ["c"],
                  "e" : ["c", "b"],
                  "f" : []
                }
        graph = Graph(graph)
        self.assertEqual(graph.neighbors('b'), ["c", "e"])

    def test_wgraph(self):
        graph = {0: [(1, 1),(2, 7)],
                  1 : [(3, 9), (5, 15)],
                  2 : [(4, 4)],
                  3 : [(4, 10), (5, 5)],
                  4 : [(5, 3)],
                  5 : []
                }
        graph = WGraph(graph)
        self.assertEqual(graph.neighbors(2), [(4, 4)])

if __name__ == '__main__':
    unittest.main()
