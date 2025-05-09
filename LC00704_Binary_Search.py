# LC00704_Binary_Search.py

# Given an array of integers nums which is sorted in ascending order, 
# and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
 

# Constraints:

# 1 <= nums.length <= 10**4
# -10**4 < nums[i], target < 10**4
# All the integers in nums are unique.
# nums is sorted in ascending order.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0]==target:
            return 0
        elif target<nums[0]:
            return -1
        
        if nums[-1]==target:
            return len(nums)-1
        elif nums[-1]<target:
            return -1
        
        left_ind=0
        right_ind=len(nums)-1

        while left_ind+1<right_ind:
            middle_ind=(left_ind+right_ind)//2
            if nums[middle_ind]==target:
                return middle_ind
            elif target<nums[middle_ind]:
                right_ind=middle_ind
            else:
                left_ind=middle_ind

        return -1
        
