# LC00529_Minesweeper.py

# Let's play the minesweeper game (Wikipedia, online game)!

# You are given an m x n char matrix board representing the game board where:

# 'M' represents an unrevealed mine,
# 'E' represents an unrevealed empty square,
# 'B' represents a revealed blank square that has no adjacent mines (i.e., above, below, left, right, and all 4 diagonals),
# digit ('1' to '8') represents how many mines are adjacent to this revealed square, and
# 'X' represents a revealed mine.
# You are also given an integer array click where click = [clickr, clickc] represents the next click position among all the unrevealed squares ('M' or 'E').

# Return the board after revealing this position according to the following rules:

# If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
# If an empty square 'E' with no adjacent mines is revealed, then change it to a revealed blank 'B' and all of its adjacent unrevealed squares should be revealed recursively.
# If an empty square 'E' with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
# Return the board when no more squares will be revealed.
 

# Example 1:


# Input: board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], click = [3,0]
# Output: [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
# Example 2:


# Input: board = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]], click = [1,2]
# Output: [["B","1","E","1","B"],["B","1","X","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
 

# Constraints:

# m == board.length
# n == board[i].length
# 1 <= m, n <= 50
# board[i][j] is either 'M', 'E', 'B', or a digit from '1' to '8'.
# click.length == 2
# 0 <= clickr < m
# 0 <= clickc < n
# board[clickr][clickc] is either 'M' or 'E'.

from collections import deque
class Solution:
    
    def count_surrounding_mines(self, board, point):
        count=0
        for row in range(max(0,point[0]-1),min(len(board),point[0]+2)):
            for col in range(max(0,point[1]-1),min(len(board[0]),point[1]+2)):
                if row==point[0] and col==point[1]:
                    continue
                if board[row][col]=='M' or board[row][col]=='X':
                    count+=1
        return count

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]]=='M':
            board[click[0]][click[1]]='X'
            return board
        #'E'
        count_mine=self.count_surrounding_mines(board, click)
        if count_mine>0:
            board[click[0]][click[1]]=str(count_mine)
        else:
            queue_B=deque()
            queue_B.append(click)
            set_visited_points=set()
            while queue_B:
                point=queue_B.popleft()
                board[point[0]][point[1]]='B'
                #check point's 8 neighbors
                #if neighbor is a new B, put it to queue
                #if neighbor is new 1-8, modify board
                for row in range(max(0,point[0]-1),min(len(board),point[0]+2)):
                    for col in range(max(0,point[1]-1),min(len(board[0]),point[1]+2)):
                        if row==point[0] and col==point[1]:
                            continue
                        if ord(board[row][col])>=ord('0') and ord(board[row][col])<=ord('8'):
                            continue
                        if board[row][col]=='B':
                            continue
                        count_mine=self.count_surrounding_mines(board,[row,col])
                        if count_mine>0:
                            board[row][col]=str(count_mine)
                        else:
                            if row*len(board[0])+col not in set_visited_points:
                                queue_B.append([row,col])
                                set_visited_points.add(row*len(board[0])+col)
        return board




