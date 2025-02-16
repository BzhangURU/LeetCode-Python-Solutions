# LC00417_Pacific_Atlantic_Water_Flow.py

# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. 
# The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the 
# island's right and bottom edges.

# The island is partitioned into a grid of square cells. You are given an m x n integer matrix 
# heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

# The island receives a lot of rain, and the rain water can flow to neighboring cells directly 
# north, south, east, and west if the neighboring cell's height is less than or equal to the 
# current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water 
# can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

# Example 1:


# Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
# Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
# [0,4]: [0,4] -> Pacific Ocean 
#        [0,4] -> Atlantic Ocean
# [1,3]: [1,3] -> [0,3] -> Pacific Ocean 
#        [1,3] -> [1,4] -> Atlantic Ocean
# [1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
#        [1,4] -> Atlantic Ocean
# [2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
#        [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
# [3,0]: [3,0] -> Pacific Ocean 
#        [3,0] -> [4,0] -> Atlantic Ocean
# [3,1]: [3,1] -> [3,0] -> Pacific Ocean 
#        [3,1] -> [4,1] -> Atlantic Ocean
# [4,0]: [4,0] -> Pacific Ocean 
#        [4,0] -> Atlantic Ocean
# Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
# Example 2:

# Input: heights = [[1]]
# Output: [[0,0]]
# Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
 

# Constraints:

# m == heights.length
# n == heights[r].length
# 1 <= m, n <= 200
# 0 <= heights[r][c] <= 10**5

# Idea: Backtrack, start from top and left rows, get all grids, that could go into Pacific, 
# Then do the same thing for Atlantic, get shared grids. 

from collections import deque

class Solution:
    def get_grids(self, heights,for_Pacific=True):
        rows=len(heights)
        cols=len(heights[0])
        set_visited_grids=set()
        my_q=deque()
        if for_Pacific:
            for r in range(1,rows):
                my_q.append((r,0))
                set_visited_grids.add((r,0))
            for c in range(cols):
                my_q.append((0,c))
                set_visited_grids.add((0,c))
        else:
            for r in range(0,rows-1):
                my_q.append((r,cols-1))
                set_visited_grids.add((r,cols-1))
            for c in range(cols):
                my_q.append((rows-1,c))
                set_visited_grids.add((rows-1,c))

        while my_q:
            q_len=len(my_q)
            for i in range(q_len):
                #search equal or higher level in 4 directions
                cur_r, cur_c=my_q.popleft()
                cur_height=heights[cur_r][cur_c]
                r_dir=[-1,1,0,0]
                c_dir=[0,0,-1,1]
                for j in range(4):
                    if cur_r+r_dir[j]>=0 and cur_r+r_dir[j]<rows and cur_c+c_dir[j]>=0 and cur_c+c_dir[j]<cols \
                            and cur_height<=heights[cur_r+r_dir[j]][cur_c+c_dir[j]] and (cur_r+r_dir[j], cur_c+c_dir[j]) not in set_visited_grids:
                        my_q.append((cur_r+r_dir[j], cur_c+c_dir[j]))
                        set_visited_grids.add((cur_r+r_dir[j], cur_c+c_dir[j]))

        return set_visited_grids



    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        set_grids_Pacific=self.get_grids(heights,True)
        set_grids_Atlantic=self.get_grids(heights,False)

        set_grids_result=set_grids_Pacific & set_grids_Atlantic

        result=[]

        for cur_r,cur_c in set_grids_result:
            result.append([cur_r,cur_c])

        return result

        
