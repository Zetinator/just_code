"""https://www.hackerrank.com/challenges/torque-and-development/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=graphs

The Ruler of HackerLand believes that every citizen of the country should have access to a library. Unfortunately, HackerLand was hit by a tornado that destroyed all of its libraries and obstructed its roads! As you are the greatest programmer of HackerLand, the ruler wants your help to repair the roads and build some new libraries efficiently.
"""

class Graph():
    """simple bidirectional graph from adjacent list
    """
    def __init__(self, n, cities):
        self.nodes = set(range(1, n+1))
        self.edges = dict()
        self.build_edges(cities)

    def build_edges(self, cities):
        for edge in cities:
            c_1, c_2 = edge
            # will be bidirectional...
            self.edges.setdefault(c_1, []).append(c_2)
            self.edges.setdefault(c_2, []).append(c_1)

    def get_neighboors(self, node):
        return self.edges.get(node, [])

    def __repr__(self):
        return repr(self.edges)


def roadsAndLibraries(n, c_lib, c_road, cities):
    """use dfs to discover the sapnning trees
    we build all the roads in the spanning tree
    and one library per tree, discovered
    """
    # special case: trivial...
    if c_lib <= c_road: return n*c_lib
    # general case: dfs
    graph = Graph(n, cities)
    parents = {}
    res = [0, 0]  # (libs, roads)
    # standard dfs...
    def dfs(node, parent):
        for neighboor in graph.get_neighboors(node):
            if neighboor not in parents:
                # increase number of roads needed
                res[1] += 1
                parents[neighboor] = node
                dfs(neighboor, node)
    # init function for the dfs...
    for city in graph.nodes:
        if city not in parents:
            parents[city] = None
            # increase number of needed libraries
            res[0] += 1
            roads = dfs(city, None)
    libs, roads = res
    return c_lib * libs + c_road * roads

# test
n, c_lib, c_road = 6, 6, 2
cities = [[1, 3],
        [3, 4],
        [2, 4],
        [1, 2],
        [2, 3],
        [5, 6]]
n, c_lib, c_road = 5,6,1
cities = [[1, 2],
        [1, 3],
        [1, 4]]

graph = Graph(n, cities)
print(f'{roadsAndLibraries(n, c_lib, c_road, cities)}')
