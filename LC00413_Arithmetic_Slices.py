# LC00413_Arithmetic_Slices.py
# An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

# For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
# Given an integer array nums, return the number of arithmetic subarrays of nums.

# A subarray is a contiguous subsequence of the array.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: 3
# Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.
# Example 2:

# Input: nums = [1]
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 5000
# -1000 <= nums[i] <= 1000

#Idea: find all key indices i where 2*nums[i]!=nums[i-1]+nums[i+1], 
#then only find AS between key indices. 
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums)<3:
            return 0
        key_indices=[]
        for i in range(len(nums)):
            if i==0 or i==len(nums)-1:
                key_indices.append(i)
            elif 2*nums[i]!=nums[i-1]+nums[i+1]:
                key_indices.append(i)
        #We can only find Arithmetic slices between two contiguous elements in key_indices
        result=0
        for i in range(len(key_indices)-1):
            if key_indices[i+1]-key_indices[i]<=1:
                continue
            #if key_indices[i+1]-key_indices[i]==5, then there are 6 points, 4 three elements AS, 3 four elements AS, ...==4+3+2+1
            result+=(key_indices[i+1]-key_indices[i])*(key_indices[i+1]-key_indices[i]-1)//2
        return result
