# LC00675_Cut_Off_Trees_for_Golf_Event.py

# You are asked to cut off all the trees in a forest for a golf event. The forest is 
# represented as an m x n matrix. In this matrix:

# 0 means the cell cannot be walked through.
# 1 represents an empty cell that can be walked through.
# A number greater than 1 represents a tree in a cell that can be walked through, 
# and this number is the tree's height.
# In one step, you can walk in any of the four directions: north, east, south, and west. 
# If you are standing in a cell with a tree, you can choose whether to cut it off.

# You must cut off the trees in order from shortest to tallest. When you cut off a tree, 
# the value at its cell becomes 1 (an empty cell).

# Starting from the point (0, 0), return the minimum steps you need to walk to cut off 
# all the trees. If you cannot cut off all the trees, return -1.

# Note: The input is generated such that no two trees have the same height, 
# and there is at least one tree needs to be cut off.

 

# Example 1:


# Input: forest = [[1,2,3],[0,0,4],[7,6,5]]
# Output: 6
# Explanation: Following the path above allows you to cut off the trees from shortest to tallest in 6 steps.
# Example 2:


# Input: forest = [[1,2,3],[0,0,0],[7,6,5]]
# Output: -1
# Explanation: The trees in the bottom row cannot be accessed as the middle row is blocked.
# Example 3:

# Input: forest = [[2,3,4],[0,0,5],[8,7,6]]
# Output: 6
# Explanation: You can follow the same path as Example 1 to cut off all the trees.
# Note that you can cut off the first tree at (0, 0) before making any steps.
 

# Constraints:

# m == forest.length
# n == forest[i].length
# 1 <= m, n <= 50
# 0 <= forest[i][j] <= 10**9
# Heights of all trees are distinct.

# Idea: Sort grid based on height, then focus on how to reach the grid with next height. 
# To avoid time limit exceed, use only one set. 

#from typing import List
from collections import deque
class Solution:
    def get_steps(self, forest, cur_pos, next_pos):
        #search path like in graph
        set_visited_grids=set()
        set_visited_grids.add(cur_pos)
        my_q=deque()
        my_q.append(cur_pos)

        steps=0
        if next_pos==cur_pos:
            return steps
        while True:
            steps+=1
            q_length=len(my_q)
            for i in range(q_length):
                grid=my_q.popleft()
                # go up, down, left, right
                row=grid[0]
                col=grid[1]
                row_dir=[0,0,-1,1]
                col_dir=[-1,1,0,0]
                for i in range(4):
                    if row==2 and col==1:
                        col=col
                    if (row+row_dir[i],col+col_dir[i])==next_pos:
                        return steps
                    if row+row_dir[i]>=0 and row+row_dir[i]<len(forest) and col+col_dir[i]>=0 and col+col_dir[i]<len(forest[0]):
                        if forest[row+row_dir[i]][col+col_dir[i]]>0 and (row+row_dir[i],col+col_dir[i]) not in set_visited_grids:
                            my_q.append((row+row_dir[i],col+col_dir[i]))
                            set_visited_grids.add((row+row_dir[i],col+col_dir[i]))

            if len(my_q)==0:
                return -1
            
    def cutOffTree(self, forest: List[List[int]]) -> int:
        sorted_grid=[]
        for row in range(len(forest)):
            for col in range(len(forest[0])):
                if forest[row][col]>1:
                    sorted_grid.append([forest[row][col],row,col])
        sorted_grid.sort(key=lambda p: p[0])

        #print(sorted_grid)

        cur_pos=[0,0]
        result=0
        for i in range(len(sorted_grid)):
            steps=self.get_steps(forest, tuple(cur_pos), tuple(sorted_grid[i][1:]))
            if steps<0:
                return -1
            cur_pos=sorted_grid[i][1:]
            #print(steps, sorted_grid[i])
            result+=steps
        return result
        
forest=[[54581641,64080174,24346381,69107959],
        [86374198,61363882,68783324,79706116],
        [668150,92178815,89819108,94701471],
        [83920491,22724204,46281641,47531096],
        [89078499,18904913,25462145,60813308]]
my_solu=Solution()
my_solu.cutOffTree(forest)
