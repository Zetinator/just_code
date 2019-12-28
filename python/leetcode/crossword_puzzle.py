"""https://www.hackerrank.com/challenges/crossword-puzzle/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=recursion-backtracking

A  Crossword grid is provided to you, along with a set of words (or names of places) which need to be filled into the grid. Cells are marked either + or -. Cells marked with a - are to be filled with the word list.
"""

def crosswordPuzzle(crossword, words):
    # preprocessing...
    words = set(words.split(';'))
    # min lenght of the words
    _min = len(min(words))
    used = set()
    to_use = lambda: words-used
    # modifiable copy...
    cross = crossword[:]
    def fill_word_row(i):
        w = max(cross[i].split('+'))
        if len(w) < _min: return
        possible_words = [word for word in to_use if len(word) >= len(w)]
        if not possible_words: return
        return (i, cross[i].index(w), lenw)
    def fill_word_column(j):
        w = max(cross[i].split('+'))
        if len(w) < _min: return False
        return (i, cross[i].index(w), lenw)


    # can we navigate into to this cell?
    def is_valid(node):
        i, j = node
        return (0 <= i < len(cross) and 0 <= j < len(cross) and
                cross[i][j] != '+')
    # can we put a word here? 
    def check_word(node, letter):
        i, j = node
        if cross[i][j] != '-': return True
        if cross[i][j] == letter: return True
        return False
    # backtracking...
    def r(current_node, word=None):
        """dfs
        """
        to_use = words - used
        if not to_use: return True
        if not is_valid(current_node): return
        for move in moves:
            next_move = moves[move](current_node)
    return

test = 6
print(f'ans: {fibonacci(test)}')
