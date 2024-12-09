# LC00581_Shortest_Unsorted_Continuous_Subarray.py

# Given an integer array nums, you need to find one continuous subarray such that 
# if you only sort this subarray in non-decreasing order, then the whole array will 
# be sorted in non-decreasing order.

# Return the shortest such subarray and output its length.

 

# Example 1:

# Input: nums = [2,6,4,8,10,9,15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
# Example 2:

# Input: nums = [1,2,3,4]
# Output: 0
# Example 3:

# Input: nums = [1]
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 10^4
# -10^5 <= nums[i] <= 10^5
 

# Follow up: Can you solve it in O(n) time complexity?

# Idea: One idea with O(nlog(n)) is to sort the array, then compare with original array
# Another idea with O(n) is to save a list--> min_from_here_to_end, then from index 0, check if here's value== min_from_here_to_end
# Also, save a list--> max_from_start_to_here.
# from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        min_from_here_to_end=[0]*len(nums)
        max_from_start_to_here=[0]*len(nums)

        max_from_start_to_here[0]=nums[0]
        for i in range(1, len(nums)):
            max_from_start_to_here[i]=max(max_from_start_to_here[i-1], nums[i])

        min_from_here_to_end[len(nums)-1]=nums[len(nums)-1]
        for i in range(len(nums)-2,-1,-1):
            min_from_here_to_end[i]=min(min_from_here_to_end[i+1], nums[i])

        left=-1
        for i in range(0,len(nums)):
            if nums[i]==min_from_here_to_end[i]:
                left=i
            else:
                break

        right=len(nums)
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==max_from_start_to_here[i]:
                right=i
            else:
                break
        
        if left+1>=right:
            return 0
        else:
            return right-left-1
        
