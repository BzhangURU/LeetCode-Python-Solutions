# LC00456_132_Pattern.py

# Given an array of n integers nums, a 132 pattern is a subsequence of three integers 
# nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

# Return true if there is a 132 pattern in nums, otherwise, return false.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: false
# Explanation: There is no 132 pattern in the sequence.
# Example 2:

# Input: nums = [3,1,4,2]
# Output: true
# Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
# Example 3:

# Input: nums = [-1,3,2,0]
# Output: true
# Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
 

# Constraints:

# n == nums.length
# 1 <= n <= 2 * 10**5
# -10**9 <= nums[i] <= 10**9

# Idea: iterate from left, we keep saving intervals that are possible [a_i,a_j] candidates
# for example: [96, 100, 86, 90, 56, 60, cur_number, ...]: the saved intervals are [96,100],[86,90],[56,60]
# when current number is BETWEEN any interval, we found the answer, 
# when current number is like 92, then we merge [86,90],[56,60] into [56, 92], and saved intervals become [96,100],[56, 92]
# So we use a stack to save intervals. (the interval on top of stack always has smallest numbers)
# [112, 112] can be an interval!!! Also, for [20,30,10,20], the saved intervals could be [20,30],[10,20]

from typing import List

from collections import deque
class Solution:
# O(n) solution
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
        
        my_stack=deque([[nums[0],nums[0]]])

        for i in range(1,len(nums)):
            cur_num=nums[i]
            top_interval=my_stack[-1]
            if top_interval[0]<cur_num and cur_num<top_interval[1]:
                return True
            elif top_interval[1]<=cur_num:
                new_interval_start=top_interval[0]
                new_interval_end=cur_num
                while len(my_stack)>0 and my_stack[-1][0]<new_interval_end:
                    if new_interval_end<my_stack[-1][1]:
                        return True
                    # we merge this interval (remove this old interval)
                    my_stack.pop()
                my_stack.append([new_interval_start,new_interval_end])
            else:
                # cur_num<=top_interval[0]
                my_stack.append([cur_num,cur_num])
        return False
                




    # O(n**2) solution:
    # def find132pattern(self, nums: List[int]) -> bool:
    #     if len(nums)<3:
    #         return False
    #     for k in range(2, len(nums)):
    #         found_i=False
    #         for i in range(k):
    #             if not found_i:
    #                 if nums[i]<nums[k]:
    #                     found_i=True
    #             else:
    #                 if nums[i]>nums[k]:
    #                     return True
                    
    #     return False




