# LC00665_Non-decreasing_Array.py

# Given an array nums with n integers, your task is to check if it could 
# become non-decreasing by modifying at most one element.

# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for 
# every i (0-based) such that (0 <= i <= n - 2).

 

# Example 1:

# Input: nums = [4,2,3]
# Output: true
# Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
# Example 2:

# Input: nums = [4,2,1]
# Output: false
# Explanation: You cannot get a non-decreasing array by modifying at most one element.
 

# Constraints:

# n == nums.length
# 1 <= n <= 10**4
# -10**5 <= nums[i] <= 10**5

# Idea: first check if bad pair number is only one, then check whether to 
# change smaller index in pair or larger index in pair. 

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums)<=1:
            return True
        bad_pair_index=-1
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                if bad_pair_index==-1:
                    bad_pair_index=i
                else:
                    return False
        
        if bad_pair_index==-1:
            return True
        if bad_pair_index==0 or (nums[bad_pair_index-1]<=nums[bad_pair_index+1]):
            return True
        if bad_pair_index==len(nums)-2 or (nums[bad_pair_index]<=nums[bad_pair_index+2]):
            return True
        return False
        

