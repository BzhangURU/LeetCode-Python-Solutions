#LC03301_Maximize_the_Total_Height_of_Unique_Towers

# You are given an array maximumHeight, where maximumHeight[i] denotes the maximum height the ith tower can be assigned.

# Your task is to assign a height to each tower so that:

# The height of the ith tower is a positive integer and does not exceed maximumHeight[i].
# No two towers have the same height.
# Return the maximum possible total sum of the tower heights. If it's not possible to assign heights, return -1.

 

# Example 1:

# Input: maximumHeight = [2,3,4,3]

# Output: 10

# Explanation:

# We can assign heights in the following way: [1, 2, 4, 3].

# Example 2:

# Input: maximumHeight = [15,10]

# Output: 25

# Explanation:

# We can assign heights in the following way: [15, 10].

# Example 3:

# Input: maximumHeight = [2,2,1]

# Output: -1

# Explanation:

# It's impossible to assign positive heights to each index so that no two towers have the same height.

 

# Constraints:

# 1 <= maximumHeight.length <= 105
# 1 <= maximumHeight[i] <= 109


#Idea: sort list from highest to lowest, then visit each tower, set it to highest possible height. 


class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        
        thresh_high_to_low=sorted(maximumHeight)
        thresh_high_to_low.reverse()

        max_possible=thresh_high_to_low[0]

        result=0
        for i in range(len(thresh_high_to_low)):
            if max_possible<=0:
                return -1
            if max_possible>thresh_high_to_low[i]:
                max_possible=thresh_high_to_low[i]
            result+=max_possible
            max_possible-=1

        return result
