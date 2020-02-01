"""this is the implementation of a standard network graph class
https://en.wikipedia.org/wiki/Graph_(abstract_data_type)#Operations
the ADT contains the following methods:
    - adjacent: are the given nodes adjacent?
    - neighbors: return list of the neighbors of the given node
    - add_node: add the node to the graph
    - capacity: returns the predefined capacity of the given edge
    - remove_node: removes the node from the graph
    - add_edge: add the edge to the graph
    - remove_edge: removes the edge from the graph
"""

class NGraph():
    def __init__(self, from_dictionary, s, t):
        self.inner = from_dictionary
        self.source = s
        self.sink = t
        self.edges = set()
        self.nodes = set()
        self.capacities = {}
        self.build()

    def __repr__(self):
        return f'graph: {repr(self.inner)}\nsource: {self.source}\nsink: {self.sink}'

    def build(self):
        """initialize edges, nodes and capacities
        """
        if not self.inner: return
        for node, links in self.inner.items():
            self.nodes.add(node)
            for neighbor, capacity in links:
                self.nodes.add(neighbor)
                self.edges.add((node, neighbor))
                self.capacities[(node, neighbor)] = capacity
        if self.source not in self.nodes:
            raise ValueError(f'source {self.source} not in the graph')
        if self.sink not in self.nodes:
            raise ValueError(f'sink {self.sink} not in the graph')

    def capacity(self, x, y):
        """returns the weight between x, y
        """
        return self.capacities.get((x, y), float('inf'))

    def adjacent(self, x, y):
        """returns True if the two give nodes are adjacent, false otherwise
        """
        if x == None or y == None: return False
        return (x, y) in self.edges or (y, x) in self.edges

    def neighbors(self, node):
        """returns a list of the neighbors of the given node
        """
        if node not in self.nodes: return []
        return [tmp[0] for tmp in self.inner.get(node, [])]
            
    def add_node(self, node):
        """adds a new node into the graph
        """
        if node == None: return
        self.nodes.add(node)
        self.inner.setdefault(node, [])
        
    def remove_node(self, node):
        """removes the given node from the graph
        """
        if node == None or node not in self.inner: return
        del(self.inner[node])
        del(self.nodes[node])

    def add_edge(self, x, y):
        """adds a new edge between the given nodes in the graph
        """
        if x == None or not y: return
        self.edges.add((x, y))

    def remove_edge(self, x, y):
        """removes the given edge from the graph
        """
        if not (x, y) in self.edges: return
        del(self.edges[(x,y)])


# test
graph = {0: [(1,5), (2,8), (3,3), (4,3), (5,7), (9,7)],
        1: [(9,4)],
        2: [(9,9)],
        3: [(6,1)],
        4: [(7,4)],
        5: [(8,6)],
        6: [(9,1)],
        7: [(9,6)],
        8: [(9,5)],
        }
graph = NGraph(graph, 0, 9)
# ford flukerson killer...
graph = {0: [(2,8), (1,8)],
        1: [(3,8)],
        2: [(3,8), (1,1)],
        }
graph = NGraph(graph, 0, 3)
