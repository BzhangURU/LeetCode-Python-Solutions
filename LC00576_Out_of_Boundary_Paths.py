# LC00576_Out_of_Boundary_Paths.py

# There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. 
# You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of 
# the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

# Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move 
# the ball out of the grid boundary. Since the answer can be very large, return it modulo 10**9 + 7.

 

# Example 1:


# Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
# Output: 6
# Example 2:


# Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
# Output: 12
 

# Constraints:

# 1 <= m, n <= 50
# 0 <= maxMove <= 50
# 0 <= startRow < m
# 0 <= startColumn < n


# Idea: Use each grid to save number of possible paths to arrive there with i steps. 
# Then keep updating by adding one to i.
# 
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        old_grid=[[0 for c in range(n)] for r in range(m)]
        old_grid[startRow][startColumn]=1
        result=0
        for move in range(maxMove):
            new_grid=[[0 for c in range(n)] for r in range(m)]

            #check each grid with positive values, spread to 4 directions
            for r in range(m):
                for c in range(n):
                    if old_grid[r][c]>0:
                        #go up
                        if r==0:
                            result+=old_grid[r][c]%(10**9+7)
                        else:
                            new_grid[r-1][c]+=old_grid[r][c]%(10**9+7)

                        #go down
                        if r==m-1:
                            result+=old_grid[r][c]
                        else:
                            new_grid[r+1][c]+=old_grid[r][c]%(10**9+7)

                        #go left
                        if c==0:
                            result+=old_grid[r][c]%(10**9+7)
                        else:
                            new_grid[r][c-1]+=old_grid[r][c]%(10**9+7)

                        #go down
                        if c==n-1:
                            result+=old_grid[r][c]%(10**9+7)
                        else:
                            new_grid[r][c+1]+=old_grid[r][c]%(10**9+7)

            old_grid=new_grid
            result=result%(10**9+7)
        return result
