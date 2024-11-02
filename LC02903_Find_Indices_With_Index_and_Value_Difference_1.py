#LC02903_Find_Indices_With_Index_and_Value_Difference_1

# You are given a 0-indexed integer array nums having length n, an integer indexDifference, and an integer valueDifference.

# Your task is to find two indices i and j, both in the range [0, n - 1], that satisfy the following conditions:

# abs(i - j) >= indexDifference, and
# abs(nums[i] - nums[j]) >= valueDifference
# Return an integer array answer, where answer = [i, j] if there are two such indices, and answer = [-1, -1] otherwise. 
# If there are multiple choices for the two indices, return any of them.

# Note: i and j may be equal.

 

# Example 1:

# Input: nums = [5,1,4,1], indexDifference = 2, valueDifference = 4
# Output: [0,3]
# Explanation: In this example, i = 0 and j = 3 can be selected.
# abs(0 - 3) >= 2 and abs(nums[0] - nums[3]) >= 4.
# Hence, a valid answer is [0,3].
# [3,0] is also a valid answer.
# Example 2:

# Input: nums = [2,1], indexDifference = 0, valueDifference = 0
# Output: [0,0]
# Explanation: In this example, i = 0 and j = 0 can be selected.
# abs(0 - 0) >= 0 and abs(nums[0] - nums[0]) >= 0.
# Hence, a valid answer is [0,0].
# Other valid answers are [0,1], [1,0], and [1,1].
# Example 3:

# Input: nums = [1,2,3], indexDifference = 2, valueDifference = 4
# Output: [-1,-1]
# Explanation: In this example, it can be shown that it is impossible to find two indices that satisfy both conditions.
# Hence, [-1,-1] is returned.
 

# Constraints:

# 1 <= n == nums.length <= 100
# 0 <= nums[i] <= 50
# 0 <= indexDifference <= 100
# 0 <= valueDifference <= 50

# Idea: create an array min_value_left_to, min_value_index_left_to to save min value and min value's index left to current index. Same for max.
# After creation, when we visit index i, we check min_value_left_to[i-indexDifference] and max_value_left_to[i-indexDifference]
from typing import List
class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        min_value_left_to=[nums[0]]*len(nums)
        min_value_index_left_to=[0]*len(nums)
        max_value_left_to=[nums[0]]*len(nums)
        max_value_index_left_to=[0]*len(nums)

        
        for i in range(1,len(nums)):
            if nums[i]< min_value_left_to[i-1]:
                min_value_left_to[i]=nums[i]
                min_value_index_left_to[i]=i
            else:
                min_value_left_to[i]=min_value_left_to[i-1]
                min_value_index_left_to[i]=min_value_index_left_to[i-1]

            if nums[i]>max_value_left_to[i-1]:
                max_value_left_to[i]=nums[i]
                max_value_index_left_to[i]=i
            else:
                max_value_left_to[i]=max_value_left_to[i-1]
                max_value_index_left_to[i]=max_value_index_left_to[i-1]

        for i in range(indexDifference,len(nums)):
            if nums[i]>=min_value_left_to[i-indexDifference]+valueDifference:
                return [min_value_index_left_to[i-indexDifference],i]
            if nums[i]<=max_value_left_to[i-indexDifference]-valueDifference:
                return [max_value_index_left_to[i-indexDifference],i]

        return [-1,-1]
