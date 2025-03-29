# LC00498_Diagonal_Traverse.py

# Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

# Example 1:

# Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,4,7,5,3,6,8,9]
# Example 2:

# Input: mat = [[1,2],[3,4]]
# Output: [1,2,3,4]

# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 10**4
# 1 <= m * n <= 10**4
# -10**5 <= mat[i][j] <= 10**5

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows=len(mat)
        cols=len(mat[0])
        num_layers=rows-1+cols-1+1
        result=[]
        for layer in range(num_layers):
            # first get start point in each layer
            if layer&1==0:
                #start from left or bottom
                if layer<=rows-1:
                    #start from left boundary
                    start_col=0
                    start_row=layer
                else:
                    #start from bottom boundary
                    start_row=rows-1
                    start_col=layer-(rows-1)
                
                while start_row>=0 and start_col<=cols-1:
                    result.append(mat[start_row][start_col])
                    start_row-=1
                    start_col+=1
            else:
                #start from top or right
                if layer<=cols-1:
                    #start from top boundary
                    start_col=layer
                    start_row=0
                else:
                    #start from right boundary
                    start_row=layer-(cols-1)
                    start_col=cols-1
                
                while start_row<=rows-1 and start_col>=0:
                    result.append(mat[start_row][start_col])
                    start_row+=1
                    start_col-=1
        return result

        





