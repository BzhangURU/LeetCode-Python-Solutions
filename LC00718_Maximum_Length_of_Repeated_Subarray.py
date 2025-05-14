# LC00718_Maximum_Length_of_Repeated_Subarray.py

# Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

 

# Example 1:

# Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
# Output: 3
# Explanation: The repeated subarray with maximum length is [3,2,1].
# Example 2:

# Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
# Output: 5
# Explanation: The repeated subarray with maximum length is [0,0,0,0,0].
 

# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 100

from typing import List

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        result=0
        for shift in range(-len(nums2)+1,len(nums1)):
            cur_count=0
            start_ind=max(0,shift)
            end_ind=min(len(nums1),len(nums2)+shift)
            for i in range(start_ind,end_ind):
                if nums1[i]==nums2[i-shift]:
                    cur_count+=1
                    if cur_count>result:
                        result=cur_count
                else:
                    cur_count=0
        return result
