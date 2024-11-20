# LC00525_Contiguous_Array.py
# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

# Example 1:

# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
# Example 2:

# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.


# Idea: iterate from start, for each index, count the total ones, and check its difference with (index+1)/2,
# save ( count_ones - (index+1)/2 ) : index   into dictionary if  ( count_ones - (index+1)/2 ) doesn't exist, 
# if exist, then calculate the index difference, that will be a candidate that has equal number of 0 and 1. 
# In the beginning, save    0: index=-1

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        my_dict={0:-1}

        count_ones=0
        result=0

        for i in range(len(nums)):
            if nums[i]==1:
                count_ones+=1
            if count_ones*2-(i+1) not in my_dict:
                my_dict[count_ones*2-(i+1)]=i
            else:
                length=i-my_dict[count_ones*2-(i+1)]
                if length>result:
                    result=length
        return result
