"""You are given a square grid with some cells open (.) and some blocked (X). Your playing piece can move along any row or column until it reaches the edge of the grid or a blocked cell. Given a grid, a start and an end position, determine the number of moves it will take to get to the end position.

You are given a square grid with some cells open (.) and some blocked (X). Your playing piece can move along any row or column until it reaches the edge of the grid or a blocked cell. Given a grid, a start and an end position, determine the number of moves it will take to get to the end position.
"""
from collections import deque

def minimumMoves(grid, startX, startY, goalX, goalY):
    """standard bfs
    """
    start, goal = (startX, startY), (goalX, goalY)
    # special case: dtart == goal
    if start == goal: return 0
    # set-up bfs
    q = deque([(start, 0)])
    parents = {}
    moves = {'right':lambda n: (n[0], n[1]+1), 
            'down':lambda n: (n[0]+1, n[1]),
            'left':lambda n: (n[0], n[1]-1),
            'up':lambda n: (n[0]-1, n[1])
            }
    def is_valid(node):
        x, y = node
        return (x < len(grid) and y < len(grid) 
                and x >= 0 and y >= 0
                and grid[x][y] == '.')
    while q:
        current_node, level = q.pop()
        # match? we are done...
        if current_node == goal: return level
        # explore... bfs wise
        for move in 'up', 'right', 'down', 'left':
            next_node = moves[move](current_node)
            while is_valid(next_node):
                # no revisiting...
                if next_node not in parents:
                    q.appendleft((next_node, level+1))
                    parents[next_node] = current_node
                next_node = moves[move](next_node)
    raise ValueError('unreachable')

# test
grid = ['.X.', '.X.', '...']
start = [0, 0]
goal = [0, 2]
grid = """XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
.......................................................................................X
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X
X....................................................................................X.X
X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X
X.X................................................................................X.X.X
X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X
X.X.X............................................................................X.X.X.X
X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X
X.X.X.X........................................................................X.X.X.X.X
X.X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X.X
X.X.X.X.X....................................................................X.X.X.X.X.X
X.X.X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X
X.X.X.X.X.X................................................................X.X.X.X.X.X.X
X.X.X.X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X.X
X.X.X.X.X.X.X............................................................X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X........................................................X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X....................................................X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X................................................X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X............................................X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X........................................X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X....................................X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X................................X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X............................X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X........................X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.XXXXXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X....................X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.XXXXXXXXXXXXXXXXXX.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X................X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.XXXXXXXXXXXXXX.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X............X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.XXXXXXXXXX.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X..........X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X..........X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X..........X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X..........X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X..........X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X..........X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X..........X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X..........X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.XXXXXXXXXXXX.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X..............X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.XXXXXXXXXXXXXXXX.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X..................X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.XXXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X......................X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.XXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X..........................X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X..............................X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X..................................X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X......................................X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X..........................................X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X..............................................X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X..................................................X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X......................................................X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X..........................................................X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X.X
X.X.X.X.X.X.X..............................................................X.X.X.X.X.X.X
X.X.X.X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X
X.X.X.X.X.X..................................................................X.X.X.X.X.X
X.X.X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X.X
X.X.X.X.X......................................................................X.X.X.X.X
X.X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X
X.X.X.X..........................................................................X.X.X.X
X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X
X.X.X..............................................................................X.X.X
X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X
X.X..................................................................................X.X
X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X
X......................................................................................X
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX""".split('\n')
start = [0, 0]
goal = [44, 44]
print(f'testing with grid:')
# for line in grid: print(line)
print(f'start: {start}, goal: {goal}')
print(f'ans: {minimumMoves(grid, *start, *goal)}')
