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
        self.generate_edges()

    def generate_edges(self):
        if not self.inner: return
        for node, neighbors in self.inner.items():
            for neighbor in neighbors:
                self.edges.add((node, neighbor))

    def adjacent(self, x, y):
        if not x or not y: return False
        return (x, y) in self.edges

    def neighbors(self, x):
        if not x or x not in self.inner: return []
        return [neighbor for neighbor in self.inner[x]]
            
    def add_node(self, x):
        if not x: return
        self.inner.setdefault(x, [])
        
    def remove_node(self, x):
        if not x or x not in self.inner: return
        del(self.inner[x])

    def add_edge(self, x, y):
        if not x or not y: return
        self.edges.add((x, y))

    def remove_edge(self, x, y):
        if not (x, y) in self.edges: return
        del(self.edges[(x,y)])

    def __repr__(self):
        return repr(self.inner)
