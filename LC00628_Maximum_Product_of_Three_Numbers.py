# LC00628_Maximum_Product_of_Three_Numbers.py

# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: 6
# Example 2:

# Input: nums = [1,2,3,4]
# Output: 24
# Example 3:

# Input: nums = [-1,-2,-3]
# Output: -6
 

# Constraints:

# 3 <= nums.length <= 10**4
# -1000 <= nums[i] <= 1000

# Idea: no negative num--> largest three
# one negative num-->largest three
# two negative nums-->largest three vs.  (min two + largest one)
# three negative nums-->largest three vs.  (min two + largest one)


#all negative nums-->largest three vs.  (min two + largest one)

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums)==3:
            return nums[0]*nums[1]*nums[2]
        
        nums.sort()
        result=nums[len(nums)-1]*nums[len(nums)-2]*nums[len(nums)-3]

        product2=nums[len(nums)-1]*nums[0]*nums[1]

        if product2>result:
            result=product2

        return result
        
