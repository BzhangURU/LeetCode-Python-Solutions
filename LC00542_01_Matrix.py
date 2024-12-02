# LC00542_01_Matrix.py

# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

# The distance between two adjacent cells is 1.

 

# Example 1:


# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]
# Example 2:


# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]
 

# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 10^4
# 1 <= m * n <= 10^4
# mat[i][j] is either 0 or 1.
# There is at least one 0 in mat.

#Idea: use a queue to save all points that have same dis to 0, from closest to furthest

from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        q=deque()
        
        rows=len(mat)
        cols=len(mat[0])
        result=[[-1 for _ in range(cols)] for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if mat[r][c]==0:
                    q.append([r,c])

        cur_dis=0
        while q:
            num_q=len(q)
            for i in range(num_q):
                [r,c]=q.popleft()
                if result[r][c]==-1:
                    result[r][c]=cur_dis
                    if r>0 and result[r-1][c]==-1:
                        q.append([r-1,c])
                    if r<rows-1 and result[r+1][c]==-1:
                        q.append([r+1,c])
                    if c>0 and result[r][c-1]==-1:
                        q.append([r,c-1])
                    if c<cols-1 and result[r][c+1]==-1:
                        q.append([r,c+1])
            cur_dis+=1

        return result
