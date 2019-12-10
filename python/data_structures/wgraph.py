"""this is the implementation of an weighted graph class
https://en.wikipedia.org/wiki/Graph_(abstract_data_type)#Operations
the ADT contains the following methods:
    - adjacent
    - neighbors
    - add_node
    - remove_node
    - add_edge
    - remove_edge
"""

class WGraph():
    def __init__(self, from_dictionary=None):
        self.inner = from_dictionary
        self.edges = set()
        self.weights = {}
        self.nodes = []
        self.generate_nodes()
        self.generate_edges()
        self.generate_weights()

    def generate_nodes(self):
        """generates a list of all the nodes between nodes
        """
        if not self.inner: return
        for node, neighbors in self.inner.items():
            self.nodes.append(node)

    def generate_edges(self):
        """generates a list of all the edges between nodes
        """
        if not self.inner: return
        for node, neighbors in self.inner.items():
            for neighbor in neighbors:
                self.edges.add((node, neighbor[0]))

    def generate_weights(self):
        """generates a list of all the edges between nodes
        """
        if not self.inner: return
        for node, neighbors in self.inner.items():
            for neighbor in neighbors:
                self.weights[(node,neighbor[0])] = neighbor[1]

    def weight(self, x, y):
        """returns the weight between x, y
        """
        if (x,y) not in self.weights: return
        return self.weights[(x, y)]

    def adjacent(self, x, y):
        """returns True if the two give nodes are adjacent, false otherwise
        """
        if x == None or y == None: return False
        return (x, y) in self.edges

    def neighbors(self, x):
        """returns a list of the neighbors of the given node
        """
        if x == None or x not in self.inner: return []
        return [neighbor[0] for neighbor in self.inner[x]]
            
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

    def __repr__(self):
        return repr(self.inner)
