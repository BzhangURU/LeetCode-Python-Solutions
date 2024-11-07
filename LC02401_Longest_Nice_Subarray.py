# LC02401_Longest_Nice_Subarray.py
# You are given an array nums consisting of positive integers.

# We call a subarray of nums nice if the bitwise AND of every pair of 
# elements that are in different positions in the subarray is equal to 0.

# Return the length of the longest nice subarray.

# A subarray is a contiguous part of an array.

# Note that subarrays of length 1 are always considered nice.

 

# Example 1:

# Input: nums = [1,3,8,48,10]
# Output: 3
# Explanation: The longest nice subarray is [3,8,48]. This subarray satisfies the conditions:
# - 3 AND 8 = 0.
# - 3 AND 48 = 0.
# - 8 AND 48 = 0.
# It can be proven that no longer nice subarray can be obtained, so we return 3.
# Example 2:

# Input: nums = [3,1,5,11,13]
# Output: 1
# Explanation: The length of the longest nice subarray is 1. Any subarray of length 1 can be chosen.
 

# Constraints:

# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9

#Use an array to count each bit's occurence in subarray
#We dont allow any bit's occurence is more than one. 

from typing import List
class class_bitwise_count_in_subarray():
    def __init__(self):
        self.bitwise_count=[0]*30
        #max_count=0
    #check any bit's occurence is still 0 or 1 if adding this num
    def check(self,num):
        index=0
        while num!=0:
            digit=num%2
            num=num//2
            if digit==1 and self.bitwise_count[index]==1:
                return False
            index+=1
        return True
    #always check before add
    def add(self,num):
        index=0
        while num!=0:
            digit=num%2
            num=num//2
            if digit==1:
                self.bitwise_count[index]+=1
            index+=1

    def remove(self,num):
        index=0
        while num!=0:
            digit=num%2
            num=num//2
            if digit==1:
                self.bitwise_count[index]-=1
            index+=1
    


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left_ind=0
        right_ind=0#right_ind is not included in subarray
        bitwise_count_in_subarray=class_bitwise_count_in_subarray()
        while right_ind<len(nums):
            if bitwise_count_in_subarray.check(nums[right_ind]):
                bitwise_count_in_subarray.add(nums[right_ind])
                right_ind+=1
            else:
                break

        result=right_ind-left_ind

        for left_ind in range(1,len(nums)):
            bitwise_count_in_subarray.remove(nums[left_ind-1])
            while right_ind<len(nums):
                if bitwise_count_in_subarray.check(nums[right_ind]):
                    bitwise_count_in_subarray.add(nums[right_ind])
                    right_ind+=1
                else:
                    break
            if result<right_ind-left_ind:
                result=right_ind-left_ind
        return result
