"""https://www.hackerrank.com/challenges/crossword-puzzle/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=recursion-backtracking

A  Crossword grid is provided to you, along with a set of words (or names of places) which need to be filled into the grid. Cells are marked either + or -. Cells marked with a - are to be filled with the word list.
"""
#!/bin/python3

import sys

def printBoard(board):
    for row in board:
        print(''.join(row))
    
def possibleDirections(board,word):
    length=len(word)
    for i in range(10):
        for j in range(10):
            possible_h = True
            possible_v = True
            for k in range(length):
                # check horizontal
                if j<10-(length-1):
                    if board[i][j+k] not in ['-',word[k]]:
                        possible_h = False
                # check vertical
                if i<10-(length-1): 
                    if board[i+k][j] not in ['-',word[k]]:
                        possible_v = False
            if possible_h and j<10-(length-1):
                yield (i,j,0)
            if possible_v and i<10-(length-1):
                yield (i,j,1)    
            
def write(board,word,startLocation):
    """write the possible word
    """
    i,j,axis=startLocation
    length=len(word)
    if axis == 0:
        for k in range(length):
            board[i][j+k]=word[k]
    else:
        for k in range(length):
            board[i+k][j]=word[k]
            
def backtrack(board,word,startLocation):
    """erase words written
    """
    i,j,axis=startLocation
    length=len(word)
    if axis == 0:
        for k in range(length):
            board[i][j+k]='-'
    else:
        for k in range(length):
            board[i+k][j]='-'
        
def solve(board,words):
    if not words:
        printBoard(board)
        return 
    word=words.pop()
    # solve...
    for direction in possibleDirections(board,word):
        write(board,word,direction)
        solve(board,words)
        backtrack(board,word,direction)
    words.append(word)
    
if __name__ == '__main__':
    board = []
    for _ in range(10):
        board_item = list(input())
        board.append(board_item)
    words = str(input()).split(";")
    solve(board,words)
