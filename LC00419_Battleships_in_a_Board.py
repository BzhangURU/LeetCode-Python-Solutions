# LC00419_Battleships_in_a_Board.py

# Given an m x n matrix board where each cell is a battleship 'X' or empty '.', 
# return the number of the battleships on board.

# Battleships can only be placed horizontally or vertically on board. In other words, 
# they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), 
# where k can be of any size. At least one horizontal or vertical cell separates between 
# two battleships (i.e., there are no adjacent battleships).

# Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
# Output: 2
# Example 2:

# Input: board = [["."]]
# Output: 0
 

# Constraints:

# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is either '.' or 'X'.
 

# Follow up: Could you do it in one-pass, using only O(1) extra memory and 
# without modifying the values board?

# Idea: we only count top left corner of each ship

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows=len(board)
        cols=len(board[0])
        count=0
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=='X':
                    if (r==0 or board[r-1][c]=='.') and (c==0 or board[r][c-1]=='.'):
                        count+=1
        return count

        

