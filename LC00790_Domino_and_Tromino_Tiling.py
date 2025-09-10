# LC00790_Domino_and_Tromino_Tiling.py

# You have two types of tiles: a 2 x 1 domino shape and a tromino shape. 
# You may rotate these shapes.


# Given an integer n, return the number of ways to tile an 2 x n board. 
# Since the answer may be very large, return it modulo 109 + 7.

# In a tiling, every square must be covered by a tile. Two tilings are different 
# if and only if there are two 4-directionally adjacent cells on the board such 
# that exactly one of the tilings has both squares occupied by a tile.

 

# Example 1:


# Input: n = 3
# Output: 5
# Explanation: The five different ways are shown above.
# Example 2:

# Input: n = 1
# Output: 1
 

# Constraints:

# 1 <= n <= 1000

# Idea: DP.  DP_with_extra_top_right[3] means 2 rows x 3 col with extra square on top right
# think more about n==3 to get solutions. 

class Solution:
    def numTilings(self, n: int) -> int:
        if n==1:
            return 1
        elif n==2:
            return 2
        DP_arr=[0]*(n+1)
        DP_arr[0]=1
        DP_arr[1]=1
        DP_arr[2]=2
        DP_with_extra_top_right=[0]*(n+1)
        DP_with_extra_top_right[1]=1
        DP_with_extra_top_right[2]=2
        DP_with_extra_bottom_right=[0]*(n+1)
        DP_with_extra_bottom_right[1]=1
        DP_with_extra_bottom_right[2]=2

        DP_with_2extra_top_right=[0]*(n+1)
        DP_with_2extra_top_right[0]=1
        DP_with_2extra_top_right[1]=1
        DP_with_2extra_top_right[2]=2
        DP_with_2extra_bottom_right=[0]*(n+1)
        DP_with_2extra_bottom_right[0]=1
        DP_with_2extra_bottom_right[1]=1
        DP_with_2extra_bottom_right[2]=2

        for i in range(3,n+1):
            DP_arr[i]=DP_arr[i-2]+DP_arr[i-1]+DP_with_extra_top_right[i-2]+DP_with_extra_bottom_right[i-2]
            DP_with_extra_top_right[i]=DP_arr[i-1]+DP_with_extra_bottom_right[i-1]
            DP_with_extra_bottom_right[i]=DP_arr[i-1]+DP_with_extra_top_right[i-1]
        return DP_arr[n]






