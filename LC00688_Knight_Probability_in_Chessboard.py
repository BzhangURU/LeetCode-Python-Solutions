# LC00688_Knight_Probability_in_Chessboard.py

# On an n x n chessboard, a knight starts at the cell (row, column) and 
# attempts to make exactly k moves. The rows and columns are 0-indexed, 
# so the top-left cell is (0, 0), and the bottom-right cell is (n - 1, n - 1).

# A chess knight has eight possible moves it can make, as illustrated below. 
# Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.


# Each time the knight is to move, it chooses one of eight possible moves uniformly at 
# random (even if the piece would go off the chessboard) and moves there.

# The knight continues moving until it has made exactly k moves or has moved off the chessboard.

# Return the probability that the knight remains on the board after it has stopped moving.

 

# Example 1:

# Input: n = 3, k = 2, row = 0, column = 0
# Output: 0.06250
# Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
# From each of those positions, there are also two moves that will keep the knight on the board.
# The total probability the knight stays on the board is 0.0625.
# Example 2:

# Input: n = 1, k = 0, row = 0, column = 0
# Output: 1.00000
 

# Constraints:

# 1 <= n <= 25
# 0 <= k <= 100
# 0 <= row, column <= n - 1

# Idea: use each grid in chess board to save count all possible moves that reach here in current step, 
# then, we also have number of all possibilities as denominator: 8**k

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp=[[0 for col in range(n)] for row in range(n)]
        dp[row][column]=1

        row_dir=[2,1, 2, 1,-2,-1,-2,-1]
        col_dir=[1,2,-1,-2, 1, 2,-1,-2]

        for i in range(k):
            dp_new=[[0 for col in range(n)] for row in range(n)]
            for row in range(n):
                for col in range(n):
                    if dp[row][col]>0:
                        for ind in range(8):
                            new_row=row+row_dir[ind]
                            new_col=col+col_dir[ind]
                            if new_row>=0 and new_row<n and new_col>=0 and new_col<n:
                                dp_new[new_row][new_col]+=dp[row][col]
            dp=dp_new
        total_sum_on_board=0
        for row in range(n):
            for col in range(n):
                total_sum_on_board+=dp[row][col]
        total_sum=8**k
        return float(total_sum_on_board)/float(total_sum)
                        



        
