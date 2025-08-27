# LC00764_Largest_Plus_Sign.py

# You are given an integer n. You have an n x n binary grid grid with all values initially 1's 
# except for some indices given in the array mines. The ith element of the array mines is defined 
# as mines[i] = [xi, yi] where grid[xi][yi] == 0.

# Return the order of the largest axis-aligned plus sign of 1's contained in grid. If there is 
# none, return 0.

# An axis-aligned plus sign of 1's of order k has some center grid[r][c] == 1 along with four arms 
# of length k - 1 going up, down, left, and right, and made of 1's. Note that there could be '
# '0's or 1's beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1's.

 

# Example 1:


# Input: n = 5, mines = [[4,2]]
# Output: 2
# Explanation: In the above grid, the largest plus sign can only be of order 2. One of them is shown.
# Example 2:


# Input: n = 1, mines = [[0,0]]
# Output: 0
# Explanation: There is no plus sign, so return 0.
 

# Constraints:

# 1 <= n <= 500
# 1 <= mines.length <= 5000
# 0 <= xi, yi < n
# All the pairs (xi, yi) are unique.

# Idea: for each grid, save its max extension only on horizontal AND only on vertical. Then iterate all grids,
# check the max of min(only on horizontal, only on vertical)
# to get a grid's max extension only on horizontal direction, get sorted mines on that row, 
# then the max extension only on horizontal direction of a grid would be its min distance to border or mines. 

from typing import List

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        grids=[[[0,0] for i in range(n)] for j in range(n)]
        for mine in mines:
            grids[mine[0]][mine[1]]=[-1,-1]
        
        #first get max extension only on horizontal

        for row in range(n):
            mines_index_on_one_row=[-1]#treat border as mine
            for col in range(n):
                if grids[row][col][0]==-1:
                    mines_index_on_one_row.append(col)
            mines_index_on_one_row.append(n)
            mine_index=0

            for col in range(n):
                if col==mines_index_on_one_row[mine_index+1]:
                    mine_index+=1
                else:
                    grids[row][col][1]=min(col-mines_index_on_one_row[mine_index],mines_index_on_one_row[mine_index+1]-col)

        for col in range(n):
            mines_index_on_one_col=[-1]#treat border as mine
            for row in range(n):
                if grids[row][col][0]==-1:
                    mines_index_on_one_col.append(row)
            mines_index_on_one_col.append(n)
            mine_index=0

            for row in range(n):
                if row==mines_index_on_one_col[mine_index+1]:
                    mine_index+=1
                else:
                    grids[row][col][0]=min(row-mines_index_on_one_col[mine_index],mines_index_on_one_col[mine_index+1]-row)

        output=0
        for row in range(n):
            for col in range(n):
                this_grid_result=min(grids[row][col][0],grids[row][col][1])
                if this_grid_result>output:
                    output=this_grid_result
        return output

            

        

