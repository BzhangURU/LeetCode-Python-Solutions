#LC03201_Find_the_Maximum_Length_of_Valid_Subsequence_1

# You are given an integer array nums.
# A 
# subsequence
#  sub of nums with length x is called valid if it satisfies:

# (sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2.
# Return the length of the longest valid subsequence of nums.

# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

# Example 1:

# Input: nums = [1,2,3,4]

# Output: 4

# Explanation:

# The longest valid subsequence is [1, 2, 3, 4].

# Example 2:

# Input: nums = [1,2,1,1,2,1,2]

# Output: 6

# Explanation:

# The longest valid subsequence is [1, 2, 1, 2, 1, 2].

# Example 3:

# Input: nums = [1,3]

# Output: 2

# Explanation:

# The longest valid subsequence is [1, 3].

 

# Constraints:

# 2 <= nums.length <= 2 * 10^5
# 1 <= nums[i] <= 10^7


#Idea: change all numbers to num%2--->0 or 1
# 4 options: 0000000...,1111111...,010101010101...,1010101010...
# if first element is 0, then only search 0101010..., otherwise only search 10101010...

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        sum1=0
        result_length=0
        for i in range(len(nums)):
            nums[i]=nums[i]%2
            sum1+=nums[i]
        if sum1>len(nums)-sum1:
            result_length=sum1
        else:
            result_length=len(nums)-sum1

        length=1
        goal=1-nums[0]
        for i in range(1,len(nums)):
            if nums[i]==goal:
                length+=1
                goal=1-goal
        if length>result_length:
            result_length=length
        return result_length
