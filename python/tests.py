import unittest
from data_structures import *
from algorithms import *


class TestDataStructures(unittest.TestCase):
    def test_avl(self):
        test = [33, 66, 1, 65, 5, 7, 41, 74, 11, 45, 14, 60, 48, 84, 85, 31, 93, 63]
        avl = AVL(test)
        self.assertEqual(avl.search(93).value, 93)

    def test_rb_tree(self):
        test = [33, 66, 1, 65, 5, 7, 41, 74, 11, 45, 14, 60, 48, 84, 85, 31, 93, 63]
        rbt = AVL(test)
        self.assertEqual(rbt.search(93).value, 93)

    def test_treap(self):
        test = [33, 66, 1, 65, 5, 7, 41, 74, 11, 45, 14, 60, 48, 84, 85, 31, 93, 63]
        treap = Treap(test)
        self.assertEqual(treap.search(93).value, 93)

    def test_splay_tree(self):
        test = [33, 66, 1, 65, 5, 7, 41, 74, 11, 45, 14, 60, 48, 84, 85, 31, 93, 63]
        splay = Treap(test)
        self.assertEqual(splay.search(93).value, 93)

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

    def test_skip_list(self):
        sl = SkipList(range(10))
        res = sl.successor(5)
        self.assertEqual(res.value, 6)

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

    def test_djs(self):
        djs = DJS()
        djs.union(10, 0)
        djs.union(11, 1)
        djs.union(12, 2)
        djs.union(10, 12)
        djs.union(11, 10)
        self.assertTrue(djs.same(11, 12))

    def test_radix_trie(self):
        keys  = 'erick quiere mucho a su marion aunque ella ya no nos quiera tanto'.split()
        rt = RTrie(keys)
        self.assertEqual(rt.predict('quier'), ['quiere','quiera'])

    def test_trie(self):
        keys  = 'erick quiere mucho a su marion aunque ella ya no nos quiera tanto'.split()
        trie = Trie(keys)
        self.assertEqual(trie.predict('quier'), ['quiere','quiera'])

    def test_fenwick_tree(self):
        test = [4, 2, 3, 3, 3, 5, 9, 2, 13, 4, 14, 4, 9, 5, 7]
        i = 3
        ft = FenwickTree(test)
        self.assertEqual(ft.sum_until(i), 9)

    def test_bitmask(self):
        state = 63
        self.assertEqual(reset(state, 3), 55)

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

    def test_uwgraph(self):
        graph = {0: [(1, 1),(2, 7)],
                  1 : [(3, 9), (5, 15)],
                  2 : [(4, 4)],
                  3 : [(4, 10), (5, 5)],
                  4 : [(5, 3)],
                  5 : []
                }
        graph = UWGraph(graph)
        self.assertEqual(graph.neighbors(2), [4])

    def test_wgraph(self):
        graph = {0: [(1, 1),(2, 7)],
                  1 : [(3, 9), (5, 15)],
                  2 : [(4, 4)],
                  3 : [(4, 10), (5, 5)],
                  4 : [(5, 3)],
                  5 : []
                }
        graph = WGraph(graph)
        self.assertEqual(graph.neighbors(2), [4])

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

    def test_bfs(self):
        g = { "a" : ["c"],
                  "b" : ["c", "e"],
                  "c" : ["a", "b", "d", "e"],
                  "d" : ["c"],
                  "e" : ["c", "b"],
                  "f" : []
                }
        g = graph.Graph(g)
        self.assertEqual(bfs(g, 'a', 'e'), ['a', 'c', 'e'])

    def test_dijkstra(self):
        graph = {0: [(1, 1),(2, 7)],
                  1 : [(3, 9), (5, 15)],
                  2 : [(4, 4)],
                  3 : [(4, 10), (5, 5)],
                  4 : [(5, 3)],
                  5 : []
                }
        graph = WGraph(graph)
        self.assertEqual(dijkstra(graph, 0, 5), [0, 2, 4, 5])

    def test_bellman_ford(self):
        graph = {0: [(1, 1),(2, 7)],
                  1 : [(3, 9), (5, 15)],
                  2 : [(4, 4)],
                  3 : [(4, 10), (5, 5)],
                  4 : [(5, 3)],
                  5 : []
                }
        graph = WGraph(graph)
        self.assertEqual(bellman_ford(graph, 0, 5), [0, 2, 4, 5])

    def test_floyd_warshall(self):
        graph = {0: [(1, 9),(2, 75)],
              1 : [(0, 9), (2, 95), (3, 19), (4, 15)],
              2 : [(0, 75), (1,95), (3, 51)],
              3 : [(1, 19), (2, 51), (4, 31)],
              4 : [(1, 15),(3, 31)],
            }
        graph = WGraph(graph)
        distances, parents = floyd_warshall(graph)
        self.assertEqual(distances[0][4], 24)

    def test_sssp_dp(self):
        graph = {0: [(1, 1),(2, 7)],
                  1 : [(3, 9), (5, 15)],
                  2 : [(4, 4)],
                  3 : [(4, 10), (5, 5)],
                  4 : [(5, 3)],
                  5 : []
                }
        graph = WGraph(graph)
        self.assertEqual(sssp_dp(graph, 0, 5), [0, 2, 4, 5])

    def test_kruskal(self):
        graph = {0: [(1, 9),(2, 75)],
                  1 : [(0, 9), (2, 95), (3, 19), (4, 15)],
                  2 : [(0, 75), (1,95), (3, 51)],
                  3 : [(1, 19), (2, 51), (4, 31)],
                  4 : [(1, 15),(3, 31)],
                }
        graph = WGraph(graph)
        self.assertEqual(kruskal(graph), {(0, 1), (3, 2), (1, 3), (4, 1)})

    def test_tarjan(self):
        graph = {0: [1],
                  1 : [3],
                  2 : [1],
                  3 : [2, 4],
                  4 : [5],
                  5 : [7],
                  6 : [4],
                  7 : [6],
                }
        graph = Graph(graph)
        self.assertEqual(tarjan(graph), [[6, 7, 5, 4], [2, 3, 1], [0]])

    def test_prim(self):
        graph = {0: [(1, 9),(2, 75)],
                  1 : [(0, 9), (2, 95), (3, 19), (4, 15)],
                  2 : [(0, 75), (1,95), (3, 51)],
                  3 : [(1, 19), (2, 51), (4, 31)],
                  4 : [(1, 15),(3, 31)],
                }
        graph = WGraph(graph)
        self.assertEqual(prim(graph), {(0, 1), (3, 2), (1, 3), (1, 4)})

    def test_dinic(self):
        graph = {0: [(2,5), (3,3)],
                1: [(4,4)],
                2: [(4,3), (1,3), (3,3)],
                3: [(1,5)],
                }
        graph = NGraph(graph, 0, 4)
        self.assertEqual(dinic(graph), 7)

    def test_welsh_powell(self):
        # https://en.wikipedia.org/wiki/Petersen_graph
        graph = {1: [5,6,2],
                2 : [1,7,3],
                3 : [2,8,4],
                4 : [5,9,3],
                5 : [1,10,4],
                6 : [8,9,1],
                7 : [2,10,9],
                8 : [3,6,10],
                9 : [7,6,4],
                10 : [5,7,8],
                }
        graph = Graph(graph)
        res = {1: 0, 2: 1, 3: 0, 4: 1, 5: 2, 6: 1, 7: 0, 8: 2, 9: 2, 10: 1}
        self.assertEqual(welsh_powell(graph), res)

    def test_gcd(self):
        n1 = 99
        n2 = 33
        self.assertEqual(gcd(n1, n2), 33)


if __name__ == '__main__':
    unittest.main()
