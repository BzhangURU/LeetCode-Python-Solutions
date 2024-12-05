# LC00565_Array_Nesting.py

# You are given an integer array nums of length n where nums is a permutation of the numbers in the range [0, n - 1].

# You should build a set s[k] = {nums[k], nums[nums[k]], nums[nums[nums[k]]], ... } subjected to the following rule:

# The first element in s[k] starts with the selection of the element nums[k] of index = k.
# The next element in s[k] should be nums[nums[k]], and then nums[nums[nums[k]]], and so on.
# We stop adding right before a duplicate element occurs in s[k].
# Return the longest length of a set s[k].

 

# Example 1:

# Input: nums = [5,4,0,3,1,6,2]
# Output: 4
# Explanation: 
# nums[0] = 5, nums[1] = 4, nums[2] = 0, nums[3] = 3, nums[4] = 1, nums[5] = 6, nums[6] = 2.
# One of the longest sets s[k]:
# s[0] = {nums[0], nums[5], nums[6], nums[2]} = {5, 6, 2, 0}
# Example 2:

# Input: nums = [0,1,2]
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 10^5
# 0 <= nums[i] < nums.length
# All the values of nums are unique.

# Idea: there are one or multiple circles formed by this method. 
# For example, if nums[i]=i, then this circle has only one element. 
# if nums[0]=1, nums[1]=0, then this circle has two elements. 
# It is not possible that there is outside branch directs to a circle(just like how to write "6"), 
# because it is a permutation, it can't point to an index twice


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited_ind=[-1]*len(nums)

        visited_ind_in_a_circle={}
        result=1

        for start_ind in range(len(nums)):
            if visited_ind[start_ind]==-1:
                #start a new circle
                path=0
                visited_ind[start_ind]=1
                ind=nums[start_ind]
                path+=1
                
                while ind !=start_ind:
                    visited_ind[ind]=1
                    ind=nums[ind]
                    path+=1
                
                circle_length=path
                if circle_length>result:
                    result=circle_length
        return result



                



