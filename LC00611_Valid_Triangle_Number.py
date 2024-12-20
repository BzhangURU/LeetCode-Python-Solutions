# LC00611_Valid_Triangle_Number.py

# Given an integer array nums, return the number of triplets chosen from 
# the array that can make triangles if we take them as side lengths of a triangle.


# Example 1:

# Input: nums = [2,2,3,4]
# Output: 3
# Explanation: Valid combinations are: 
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3
# Example 2:

# Input: nums = [4,2,3,4]
# Output: 4
 

# Constraints:

# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000


class Solution(object):
    def num_qualified_third_edge(self, nums,i,j):
        #find the largest index k that nums[k]<nums[i]+nums[j] start from j
        left_ind=j
        right_ind=len(nums)-1
        if j>=len(nums)-1:
            return 0
        if nums[right_ind]<nums[i]+nums[j]:
            return len(nums)-1-j
        while left_ind+1<right_ind:
            middle_ind=int((left_ind+right_ind)//2)
            if nums[middle_ind]<nums[i]+nums[j]:
                left_ind=middle_ind
            else:
                right_ind=middle_ind
        return left_ind-j


    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=0
        nums.sort()
        for i in range(len(nums)):
            if nums[i]<=0:
                continue

            for j in range(i+1, len(nums)):
                result+=self.num_qualified_third_edge(nums,i,j)
        return result
