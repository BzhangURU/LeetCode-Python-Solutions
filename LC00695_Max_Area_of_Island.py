# LC00695_Max_Area_of_Island.py

# You are given an m x n binary matrix grid. An island is a group of 1's 
# (representing land) connected 4-directionally (horizontal or vertical.) 
# You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

 

# Example 1:


# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#                [0,0,0,0,0,0,0,1,1,1,0,0,0],
#                [0,1,1,0,1,0,0,0,0,0,0,0,0],
#                [0,1,0,0,1,1,0,0,1,0,1,0,0],
#                [0,1,0,0,1,1,0,0,1,1,1,0,0],
#                [0,0,0,0,0,0,0,0,0,0,1,0,0],
#                [0,0,0,0,0,0,0,1,1,1,0,0,0],
#                [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.
# Example 2:

# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0 or 1.

from collections import deque

class Solution:
    def getAreaFrom(self,grid,rows,cols,r,c):
        my_set=set()
        my_set.add((r,c))
        my_q=deque()
        my_q.append((r,c))
        area=0

        row_dir=[0,0,-1,1]
        col_dir=[1,-1,0,0]
        while my_q:
            row,col=my_q.popleft()
            grid[row][col]=2
            area+=1
            for i in range(4):
                new_row=row+row_dir[i]
                new_col=col+col_dir[i]
                if new_row>=0 and new_row<rows and \
                new_col>=0 and new_col<cols and \
                grid[new_row][new_col]==1 and (new_row,new_col) not in my_set:
                    my_q.append((new_row,new_col))
                    my_set.add((new_row,new_col))
        return area
                    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])

        maxArea=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    area=self.getAreaFrom(grid,rows,cols,r,c)
                    if area>maxArea:
                        maxArea=area
        return maxArea




