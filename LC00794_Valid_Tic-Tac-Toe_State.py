# LC00794_Valid_Tic-Tac-Toe_State.py

# Given a Tic-Tac-Toe board as a string array board, return true if and only if it is possible to 
# reach this board position during the course of a valid tic-tac-toe game.

# The board is a 3 x 3 array that consists of characters ' ', 'X', and 'O'. The ' ' character 
# represents an empty square.

# Here are the rules of Tic-Tac-Toe:

# Players take turns placing characters into empty squares ' '.
# The first player always places 'X' characters, while the second player always places 'O' characters.
# 'X' and 'O' characters are always placed into empty squares, never filled ones.
# The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
# The game also ends if all squares are non-empty.
# No more moves can be played if the game is over.
 

# Example 1:


# Input: board = ["O  ","   ","   "]
# Output: false
# Explanation: The first player always plays "X".
# Example 2:


# Input: board = ["XOX"," X ","   "]
# Output: false
# Explanation: Players take turns making moves.
# Example 3:


# Input: board = ["XOX","O O","XOX"]
# Output: true
 

# Constraints:

# board.length == 3
# board[i].length == 3
# board[i][j] is either 'X', 'O', or ' '.

# Alert: ["XXX",
#         "   ",
#         "OOO"]

# Alert: ["XXX",
#         "XOO",
#         "OO "]


class Solution:
    def win_of(self,char_XO,board):
        if board[0][0]==board[0][1]==board[0][2]==char_XO:
            return True
        if board[1][0]==board[1][1]==board[1][2]==char_XO:
            return True
        if board[2][0]==board[2][1]==board[2][2]==char_XO:
            return True
        if board[0][0]==board[1][0]==board[2][0]==char_XO:
            return True
        if board[0][1]==board[1][1]==board[2][1]==char_XO:
            return True
        if board[0][2]==board[1][2]==board[2][2]==char_XO:
            return True
        if board[0][0]==board[1][1]==board[2][2]==char_XO:
            return True
        if board[2][0]==board[1][1]==board[0][2]==char_XO:
            return True
        return False
    def validTicTacToe(self, board: List[str]) -> bool:
        count_X=board[0].count('X')+board[1].count('X')+board[2].count('X')
        count_O=board[0].count('O')+board[1].count('O')+board[2].count('O')

        if count_X<count_O or count_X>count_O+1:
            return False
        
        if self.win_of('X',board):
            if count_X==count_O:
                return False
            if self.win_of('O',board):
                return False
            
        if self.win_of('O',board):
            if count_X==count_O+1:
                return False

        return True
        
