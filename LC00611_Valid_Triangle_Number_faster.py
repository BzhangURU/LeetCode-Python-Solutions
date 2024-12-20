# LC00611_Valid_Triangle_Number.py

# Given an integer array nums, return the number of triplets chosen from 
# the array that can make triangles if we take them as side lengths of a triangle.


# Example 1:

# Input: nums = [2,2,3,4]
# Output: 3
# Explanation: Valid combinations are: 
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3
# Example 2:

# Input: nums = [4,2,3,4]
# Output: 4
 

# Constraints:

# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000


class Solution(object):
    
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=0
        nums.sort()
        #assume i,j,k order
        for k in range(2, len(nums)):
            i=0
            j=k-1
            while i<j:
                if nums[i]+nums[j]<=nums[k]:
                    #j is already the possible largest, so i is too small
                    i+=1
                else:
                    # in here, nums[i]+nums[j]>nums[k], if we fix j, then i-->i, i+1, ..., j-1 can always form triangle
                    result+=j-i
                    #decrease j to search other possibility, because array is sorted, so the possible i can only increase, not decrease.
                    j-=1
        return result
