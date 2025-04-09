# LC00673_Number_of_Longest_Increasing_Subsequence.py

# Given an integer array nums, return the number of longest increasing subsequences.

# Notice that the sequence has to be strictly increasing.

 

# Example 1:

# Input: nums = [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
# Example 2:

# Input: nums = [2,2,2,2,2]
# Output: 5
# Explanation: The length of the longest increasing subsequence is 1, and 
# there are 5 increasing subsequences of length 1, so output 5.
 

# Constraints:

# 1 <= nums.length <= 2000
# -10**6 <= nums[i] <= 10**6
# The answer is guaranteed to fit inside a 32-bit integer.

# Idea: DP. For each index, save the length of longest subsequence that ends with this index, and the number. 
# When iterate the next index, get answer based on previous DP results. 

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        DP=[[1,1]]#max length, count

        for i in range(1,len(nums)):
            DP.append([1,1])
            for j in range(i):
                if nums[j]<nums[i] and DP[i][0]<DP[j][0]+1:
                    DP[i][0]=DP[j][0]+1
                    DP[i][1]=DP[j][1]
                elif nums[j]<nums[i] and DP[i][0]==DP[j][0]+1:
                    DP[i][1]+=DP[j][1]

        max_length=-1
        max_length_count=0

        for i in range(len(nums)):
            if DP[i][0]>max_length:
                max_length=DP[i][0]
                max_length_count=DP[i][1]
            elif DP[i][0]==max_length:
                max_length_count+=DP[i][1]

        return max_length_count


        

