# LC00643_Maximum_Average_Subarray_I.py

# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average 
# value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000
 

# Constraints:

# n == nums.length
# 1 <= k <= n <= 10**5
# -10**4 <= nums[i] <= 10**4

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        cur_sum=0
        max_sum=0
        for i in range(len(nums)):
            if i<k:
                cur_sum+=nums[i]
                if i==k-1:
                    max_sum=cur_sum
            else:
                cur_sum+=nums[i]
                cur_sum-=nums[i-k]
                if max_sum<cur_sum:
                    max_sum=cur_sum

        return float(max_sum)/float(k)

        
