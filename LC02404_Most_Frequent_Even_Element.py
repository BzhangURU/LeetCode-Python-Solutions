

# LC02404_Most_Frequent_Even_Element.py

# Given an integer array nums, return the most frequent even element.

# If there is a tie, return the smallest one. If there is no such element, return -1.

 

# Example 1:

# Input: nums = [0,1,2,2,4,4,1]
# Output: 2
# Explanation:
# The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
# We return the smallest one, which is 2.
# Example 2:

# Input: nums = [4,4,4,9,2,4]
# Output: 4
# Explanation: 4 is the even element appears the most.
# Example 3:

# Input: nums = [29,47,21,41,13,37,25,7]
# Output: -1
# Explanation: There is no even element.
 

# Constraints:

# 1 <= nums.length <= 2000
# 0 <= nums[i] <= 10^5

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        dict_num_freq={}
        max_num_freq=-1
        result=-1

        for i in range(len(nums)):
            if nums[i] & 1 ==0:
                if nums[i] in dict_num_freq:
                    freq=dict_num_freq[nums[i]]+1
                    dict_num_freq[nums[i]]=freq
                    if freq> max_num_freq:
                        max_num_freq=freq
                        result=nums[i]
                    elif freq == max_num_freq and nums[i]<result:
                        result=nums[i]
                else:
                    dict_num_freq[nums[i]]=1
                    if max_num_freq<1:
                        max_num_freq=1
                        result=nums[i]
                    elif max_num_freq==1 and nums[i]<result:
                        result=nums[i]

        return result
