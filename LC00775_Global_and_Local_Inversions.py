# LC00775_Global_and_Local_Inversions.py

# You are given an integer array nums of length n which represents a permutation of 
# all the integers in the range [0, n - 1].

# The number of global inversions is the number of the different pairs (i, j) where:

# 0 <= i < j < n
# nums[i] > nums[j]
# The number of local inversions is the number of indices i where:

# 0 <= i < n - 1
# nums[i] > nums[i + 1]
# Return true if the number of global inversions is equal to the number of local inversions.

 

# Example 1:

# Input: nums = [1,0,2]
# Output: true
# Explanation: There is 1 global inversion and 1 local inversion.
# Example 2:

# Input: nums = [1,2,0]
# Output: false
# Explanation: There are 2 global inversions and 1 local inversion.
 

# Constraints:

# n == nums.length
# 1 <= n <= 10**5
# 0 <= nums[i] < n
# All the integers of nums are unique.
# nums is a permutation of all the numbers in the range [0, n - 1].

# Idea: local inversions is subset of global inversions. First think about position of largest num, it should be 
# put into last position or second to last position, otherwise it will introduce extra global inversion. 
# Then think about second largest num, if largest num is at second to last position, then second largest num
# has to be put into last position, otherwise it will introduce extra global inversion. So we have handled the 
# largest two nums, and we contiue this deduction. 
# For example, the permutation need to be like: 0 |  2 1 | 4 3 |  5 | 6 | 7 | 9 8 | ...

from typing import List

class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        i=0
        n=len(nums)
        if n==1:
            return True
        while i<n:
            if i!=nums[i]:
                if i!=nums[i+1] or i==n-1:
                    return False
                else:
                    if i+1 != nums[i]:
                        return False
                    else:
                        i+=1
            i+=1
        return True
        

