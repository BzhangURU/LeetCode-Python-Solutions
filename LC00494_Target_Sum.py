# LC00494_Target_Sum.py

# You are given an integer array nums and an integer target.

# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target.

 

# Example 1:

# Input: nums = [1,1,1,1,1], target = 3
# Output: 5
# Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
# Example 2:

# Input: nums = [1], target = 1
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 20
# 0 <= nums[i] <= 1000
# 0 <= sum(nums[i]) <= 1000
# -1000 <= target <= 1000
from typing import List
class Solution:
    def num_of_dif_exp(self, nums, last_element_ind, target, dynamic_sum):
        result=0
        if last_element_ind==0:
            if nums[0]==target:
                result+=1
            if -nums[0]==target:
                result+=1
            return result
        if abs(target)>dynamic_sum[last_element_ind]:
            return 0
        result1=self.num_of_dif_exp(nums,last_element_ind-1,target+nums[last_element_ind],dynamic_sum)
        result2=self.num_of_dif_exp(nums,last_element_ind-1,target-nums[last_element_ind],dynamic_sum)
        return result1+result2
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        nums.sort()
        dynamic_sum=[0]*len(nums)
        for i in range(len(nums)):
            if i==0:
                dynamic_sum[0]=nums[0]
            else:
                dynamic_sum[i]=dynamic_sum[i-1]+nums[i]
        return self.num_of_dif_exp(nums, len(nums)-1, target, dynamic_sum)
    
#dp[i][target]=dp[i-1][target+nums[i]]+dp[i-1][target-nums[i]]
        
