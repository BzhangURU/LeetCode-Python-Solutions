# LC00689_Maximum_Sum_of_3_Non-Overlapping_Subarrays.py

# Given an integer array nums and an integer k, find three non-overlapping subarrays 
# of length k with maximum sum and return them.

# Return the result as a list of indices representing the starting position of each 
# interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

 

# Example 1:

# Input: nums = [1,2,1,2,6,7,5,1], k = 2
# Output: [0,3,5]
# Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
# We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically smaller.
# Example 2:

# Input: nums = [1,2,1,2,1,2,1,2,1], k = 2
# Output: [0,2,4]
 

# Constraints:

# 1 <= nums.length <= 2 * 10**4
# 1 <= nums[i] < 2**16
# 1 <= k <= floor(nums.length / 3)

# Idea: first, pre-calculate all sums of length k arrays to form a list k_sum, 
# then pre-calculate the max value's position before and after different indexes in k_sum
# In this problem, we need to find three indexes in k_sum that is largest, and also the indexes are 
# at least k-distance away from each other
# then, iterate through the index i of middle one, then find the max before i-k and max after i+k.
from typing import List
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        accumulated_sum=[nums[0]]
        for i in range(1, len(nums)):
            new_sum=accumulated_sum[-1]+nums[i]
            accumulated_sum.append(new_sum)

        k_sum=[0]*(len(nums)-k+1)
        for i in range(len(nums)-k+1):
            if i==0:
                k_sum[0]=accumulated_sum[k-1]
            else:
                k_sum[i]=accumulated_sum[i+k-1]-accumulated_sum[i-1]

        max_values_index_before=[0]*(len(nums)-k+1)
        max_values_index_since=[len(nums)-k]*(len(nums)-k+1)
        
        for i in range(1, len(nums)-k+1-2*k):
            if k_sum[i]>k_sum[max_values_index_before[i-1]]:
                max_values_index_before[i]=i
            else:
                max_values_index_before[i]=max_values_index_before[i-1]

        for i in range(len(nums)-k-1, 2*k-1, -1):
            #use '>=', not '>' to have smaller index
            #set to 2*k-1, not 2*k, as we are reaching until 2k
            if k_sum[i]>=k_sum[max_values_index_since[i+1]]:
                max_values_index_since[i]=i
            else:
                max_values_index_since[i]=max_values_index_since[i+1]

        print(k_sum)
        print(max_values_index_before)
        print(max_values_index_since)

        result=[0,k,2*k]
        for middle_ind in range(k,len(k_sum)-k):
            left_ind=max_values_index_before[middle_ind-k]
            right_ind=max_values_index_since[middle_ind+k]
            if k_sum[left_ind]+k_sum[middle_ind]+k_sum[right_ind]>k_sum[result[0]]+k_sum[result[1]]+k_sum[result[2]]:
                result=[left_ind,middle_ind,right_ind]
        return result
    
my_solu=Solution()
nums=[17,7,19,11,1,19,17,6,13,18,2,7,12,16,16,18,9,3,19,5]
print(my_solu.maxSumOfThreeSubarrays(nums,6))




        
