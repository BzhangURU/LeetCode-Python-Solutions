# LC00594_Longest_Harmonious_Subsequence.py

# We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

# Given an integer array nums, return the length of its longest harmonious 
# subsequence
#  among all its possible subsequences.

 

# Example 1:

# Input: nums = [1,3,2,2,5,2,3,7]

# Output: 5

# Explanation:

# The longest harmonious subsequence is [3,2,2,2,3].

# Example 2:

# Input: nums = [1,2,3,4]

# Output: 2

# Explanation:

# The longest harmonious subsequences are [1,2], [2,3], and [3,4], all of which have a length of 2.

# Example 3:

# Input: nums = [1,1,1,1]

# Output: 0

# Explanation:

# No harmonic subsequence exists.

 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -109 <= nums[i] <= 109

# Idea: use a dict to save number and its frequency


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        my_dict={}
        for i in range(len(nums)):
            if nums[i] not in my_dict:
                my_dict[nums[i]]=1
            else:
                my_dict[nums[i]]+=1
        result=0
        for k, v in my_dict.items():
            if k+1 in my_dict:
                cur_res=v+my_dict[k+1]
                if cur_res>result:
                    result=cur_res
        return result
        
