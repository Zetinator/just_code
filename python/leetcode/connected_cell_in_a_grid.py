"""https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=graphs

Consider a matrix where each cell contains either a 0 or a 1 and any cell containing a  is called a filled cell. Two cells are said to be connected if they are adjacent to each other horizontally, vertically, or diagonally. In the diagram below, the two colored regions show cells connected to the filled cells. Black on white are not connected.
"""

def maxRegion(grid):
    """classic paint...
    backtracking solution
    """
    maxRegion.max = 0
    parents = {}
    # set of possible moves
    moves = {'up':lambda node: (node[0]+1, node[1]),
            'down':lambda node: (node[0]-1, node[1]),
            'down-right':lambda node: (node[0]-1, node[1]+1),
            'down-left':lambda node: (node[0]-1, node[1]-1),
            'up-right':lambda node: (node[0]+1, node[1]+1),
            'up-left':lambda node: (node[0]+1, node[1]-1),
            'right':lambda node: (node[0], node[1]+1),
            'left':lambda node: (node[0], node[1]-1),
            }
    def is_valid(node):
        """is the next move possible?
        """
        i, j = node
        if node in parents: return
        return (0 <= i < len(grid) and 0 <= j < len(grid[0])
                and grid[i][j] == 1)
    def bfs(start):
        """standard bfs
        """
        # no revisiting...
        if start in parents: return
        # set-up
        parents[start] = None
        frontier = [start]
        current_region = 1
        while frontier:
            _next = []
            for current_node in frontier:
                for move in moves:
                    next_move = moves[move](current_node)
                    if is_valid(next_move):
                        parents[next_move] = current_node
                        _next.append(next_move)
                        current_region += 1
            frontier = _next
        # update the global max
        maxRegion.max = max(maxRegion.max, current_region)
    # try all the nodes with 1s
    for i,line in enumerate(grid):
        for j, e in enumerate(line):
            if e:
                bfs((i,j))
    return maxRegion.max

# test
grid = """1 1 0 0
0 1 1 0
0 0 1 0
1 0 0 0"""

grid = """0 1 1 1 1
1 0 0 0 1
1 1 0 1 0
0 1 0 1 1
0 1 1 1 0"""

_grid = []
for line in grid.split('\n'):
    tmp = []
    for n in line.split():
        tmp.append(int(n))
    _grid.append(tmp)
grid = _grid
print(f'griding with: {grid}')
print(f'ans: {maxRegion(grid)}')

