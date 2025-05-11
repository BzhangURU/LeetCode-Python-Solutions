# LC00713_Subarray_Product_Less_Than_K.py

# Given an array of integers nums and an integer k, return the number of contiguous subarrays 
# where the product of all the elements in the subarray is strictly less than k.

 

# Example 1:

# Input: nums = [10,5,2,6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
# Example 2:

# Input: nums = [1,2,3], k = 0
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 3 * 10**4
# 1 <= nums[i] <= 1000
# 0 <= k <= 10**6

from typing import List

#Idea: two sum

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k==0:
            return 0
        result=0
        if nums[0]<k:
            left_ind=0
            right_ind=0
            cur_product=nums[0]
        else:
            i=1
            while nums[i]>=k:
                i+=1
                if i>=len(nums):
                    return 0
            left_ind=i
            right_ind=i
            cur_product=nums[i]

        while right_ind+1<len(nums) and cur_product*nums[right_ind+1]<k:
            right_ind+=1
            cur_product*=nums[right_ind]

        result+=(1  +  right_ind-left_ind+1)*(right_ind-left_ind+1)//2
        #print(left_ind,right_ind,result)

        while right_ind+1<len(nums):
            right_ind+=1
            cur_product*=nums[right_ind]

            while cur_product>=k and left_ind<=right_ind:
                cur_product=cur_product//nums[left_ind]
                left_ind+=1
            
            if left_ind<=right_ind:
                result+=right_ind-left_ind+1
                #print(left_ind,right_ind,right_ind-left_ind+1)

        return result

nums = [10,5,2,6]
k=100
nums=[1,1,1]
k=2
my_solu=Solution()
my_solu.numSubarrayProductLessThanK(nums,k)

        


