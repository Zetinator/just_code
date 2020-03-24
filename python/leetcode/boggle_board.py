"""https://www.geeksforgeeks.org/boggle-find-possible-words-board-characters/
Boggle (Find all possible words in a board of characters)
Given a dictionary, a method to do lookup in dictionary and a M x N board where every cell has one character. Find all possible words that can be formed by a sequence of adjacent characters. Note that we can move to any of 8 adjacent characters, but a word should not have multiple instances of same cell.

Example:

Input: dictionary[] = {"GEEKS", "FOR", "QUIZ", "GO"};
       boggle[][]   = {{'G', 'I', 'Z'},
                       {'U', 'E', 'K'},
                       {'Q', 'S', 'E'}};
      isWord(str): returns true if str is present in dictionary
                   else false.

Output:  Following words of dictionary are present
         GEEKS
         QUIZ
"""
def boggle(board: list, dictionary: set)-> list:
    """navigate trough the graph, testing with raytrace in the eight directions
    """
    if not board or not all([any(row) for row in board]): raise ValueError('empty input...')
    # test if the position is valid
    def valid(node):
        x, y = node
        if not 0 <= x < len(board) or not 0 <= y < len(board[0]): return False
        return True
    # define moves to traverse the graph
    moves = {
            'up': lambda node: (node[0]-1, node[1]),
            'down': lambda node: (node[0]+1, node[1]),
            'left': lambda node: (node[0], node[1]-1),
            'right': lambda node: (node[0], node[1]+1),
            'upper_l': lambda node: (node[0]-1, node[1]-1),
            'upper_r': lambda node: (node[0]-1, node[1]+1),
            'lower_l': lambda node: (node[0]+1, node[1]-1),
            'lower_r': lambda node: (node[0]+1, node[1]+1),
            }
    # variable to return
    words_present = set()
    # raytrace for words in the dict
    def raygun(start):
        for k, move in moves.items():
            row, column = node = start
            raytrace = [board[row][column]]
            while raytrace and valid(move(node)):
                row, column = node = move(node)
                raytrace.append(board[row][column])
                current_word = ''.join(raytrace)
                # print(f'status: ray:{raytrace}, node:{node}, current_word: {current_word}')
                if current_word in dictionary: words_present.add(current_word)
    for i, row in enumerate(board):
        for j, letter in enumerate(row):
            raygun((i,j))
    return words_present

# test
dictionary = set(["GEE", "FOR", "QUIZ", "SEI"])
board = [
        ['G', 'I', 'Z'],
        ['U', 'E', 'K'],
        ['Q', 'S', 'E']
        ]
print(f'board:')
for row in board: print(row)
print(f'from: {dictionary}, the words present in the board are: {boggle(board, dictionary)}')

