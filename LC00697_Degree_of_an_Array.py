# LC00697_Degree_of_an_Array.py

# Given a non-empty array of non-negative integers nums, the degree of this array 
# is defined as the maximum frequency of any one of its elements.

# Your task is to find the smallest possible length of a (contiguous) subarray of 
# nums, that has the same degree as nums.

 

# Example 1:

# Input: nums = [1,2,2,3,1]
# Output: 2
# Explanation: 
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
# Example 2:

# Input: nums = [1,2,2,3,1,4,2]
# Output: 6
# Explanation: 
# The degree is 3 because the element 2 is repeated 3 times.
# So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
 

# Constraints:

# nums.length will be between 1 and 50,000.
# nums[i] will be an integer between 0 and 49,999.

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # use a dictionary to save num: [freq, smallest_ind, largest_ind]
        num_dict={}
        max_freq=0
        for i in range(len(nums)):
            if nums[i] not in num_dict:
                num_dict[nums[i]]=[1,i,i]
            else:
                num_dict[nums[i]][0]+=1
                num_dict[nums[i]][2]=i
            if max_freq<num_dict[nums[i]][0]:
                max_freq=num_dict[nums[i]][0]

        result=len(nums)
        for num,v in num_dict.items():
            if v[0]==max_freq and v[2]-v[1]+1<result:
                result=v[2]-v[1]+1
        return result



        
