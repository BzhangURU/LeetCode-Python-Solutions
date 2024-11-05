
# LC02501_Longest_Square_Streak_in_an_Array.py
# You are given an integer array nums. A subsequence of nums is called a square streak if:

# The length of the subsequence is at least 2, and
# after sorting the subsequence, each element (except the first element) is the square of the previous number.
# Return the length of the longest square streak in nums, or return -1 if there is no square streak.

# A subsequence is an array that can be derived from another array by deleting some or no elements 
# without changing the order of the remaining elements.

 

# Example 1:

# Input: nums = [4,3,6,16,8,2]
# Output: 3
# Explanation: Choose the subsequence [4,16,2]. After sorting it, it becomes [2,4,16].
# - 4 = 2 * 2.
# - 16 = 4 * 4.
# Therefore, [4,16,2] is a square streak.
# It can be shown that every subsequence of length 4 is not a square streak.
# Example 2:

# Input: nums = [2,3,5,6,7]
# Output: -1
# Explanation: There is no square streak in nums so return -1.
 

# Constraints:

# 2 <= nums.length <= 10^5
# 2 <= nums[i] <= 10^5

def largest_in_a_square_streak(num,my_set):
    #get the largest num in a square streak
    while num*num in my_set:
        num=num*num
    return num

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        my_set=set()
        for i in range(len(nums)):
            if nums[i] not in my_set:
                my_set.add(nums[i])
        result=1
        dict_key_largest_value_length={}
        #key is largest num in a square streak, value is square streak's length
        for num in my_set:
            largest=largest_in_a_square_streak(num,my_set)
            if largest not in dict_key_largest_value_length:
                dict_key_largest_value_length[largest]=1
            else:
                cur_length=dict_key_largest_value_length[largest]
                cur_length+=1
                dict_key_largest_value_length[largest]=cur_length
                if result<cur_length:
                    result=cur_length
            
        if result==1:
            return -1
        else:
            return result
