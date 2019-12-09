"""this is the implementation of an unweighted graph class
https://en.wikipedia.org/wiki/Graph_(abstract_data_type)#Operations
the ADT contains the following methods:
    - adjacent
    - neighbors
    - add_node
    - remove_node
    - add_edge
    - remove_edge
"""

class Graph():
    def __init__(self, from_dictionary=None):
        self.inner = from_dictionary
        self.nodes = []
        self.edges = set()
        self.generate_edges()
        self.generate_nodes()

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
                self.edges.add((node, neighbor))

    def adjacent(self, x, y):
        """returns True if the two give nodes are adjacent, false otherwise
        """
        if not x or not y: return False
        return (x, y) in self.edges

    def neighbors(self, x):
        """returns a list of the neighbors of the given node
        """
        if not x or x not in self.inner: return []
        return [neighbor for neighbor in self.inner[x]]
            
    def add_node(self, x):
        """adds a new node into the graph
        """
        if not x: return
        self.inner.setdefault(x, [])
        
    def remove_node(self, x):
        """removes the given node from the graph
        """
        if not x or x not in self.inner: return
        del(self.inner[x])

    def add_edge(self, x, y):
        """adds a new edge between the given nodes in the graph
        """
        if not x or not y: return
        self.edges.add((x, y))

    def remove_edge(self, x, y):
        """removes the given edge from the graph
        """
        if not (x, y) in self.edges: return
        del(self.edges[(x,y)])

    def __repr__(self):
        return repr(self.inner)
