"""this is the implementation of an unweighted and undirected graph class
https://en.wikipedia.org/wiki/Graph_(abstract_data_type)#Operations
the ADT contains the following methods:
    - adjacent
    - neighbors
    - add_node
    - remove_node
    - add_edge
    - remove_edge
"""

class UGraph():
    def __init__(self, from_dictionary=None):
        self.inner = from_dictionary
        self.nodes = set()
        self.edges = set()
        self.build()

    def __repr__(self):
        return f'graph: {repr(self.inner)}'

    def build(self):
        """initialize edges, nodes and capacities
        """
        if not self.inner: return
        for node, neighbors in self.inner.items():
            self.nodes.add(node)
            for neighbor in neighbors:
                self.nodes.add(neighbor)
                self.edges.add((node, neighbor))

    def adjacent(self, x, y):
        """returns True if the two give nodes are adjacent, false otherwise
        """
        if x == None or y == None: return False
        return (x, y) in self.edges or (y, x) in self.edges

    def neighbors(self, node):
        """returns a list of the neighbors of the given node
        """
        if node not in self.nodes: return []
        return [tmp for tmp in self.inner.get(node, [])]
            
    def add_node(self, x):
        """adds a new node into the graph
        """
        if x == None: return
        self.inner.setdefault(x, [])
        
    def remove_node(self, x):
        """removes the given node from the graph
        """
        if x == None or x not in self.inner: return
        del(self.inner[x])

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
