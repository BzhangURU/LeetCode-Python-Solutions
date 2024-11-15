# LC0523_Continuous_Subarray_Sum.py
# Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

# A good subarray is a subarray where:

# its length is at least two, and
# the sum of the elements of the subarray is a multiple of k.
# Note that:

# A subarray is a contiguous part of the array.
# An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
 

# Example 1:

# Input: nums = [23,2,4,6,7], k = 6
# Output: true
# Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
# Example 2:

# Input: nums = [23,2,6,4,7], k = 6
# Output: true
# Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
# 42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
# Example 3:

# Input: nums = [23,2,6,4,7], k = 13
# Output: false
 

# Constraints:

# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^9
# 0 <= sum(nums[i]) <= 2^31 - 1
# 1 <= k <= 2^31 - 1

# Idea: get accumulated sum, and save remainder of sum divided by k to a set, if the remainder occurs again, then return True
# Keep in mind the constrain that good array should have len>=2

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        list_sum_before=[0]*(len(nums)+1)
        
        list_sum_before[0]=0
        list_sum_before[1]=nums[0]
        my_sum=nums[0]
        set_remainders={0}
        last_remainder=nums[0]%k
        for i in range(2,len(nums)+1):
            my_sum+=nums[i-1]
            list_sum_before[i]=my_sum
            remainder=my_sum%k
            if remainder in set_remainders:
                return True
            #we only put last remainder because of constraint len>=2
            set_remainders.add(last_remainder)
            last_remainder=remainder

        return False
