# LC00645_Set_Mismatch.py

# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, 
# due to some error, one of the numbers in s got duplicated to another number in the set, which results 
# in repetition of one number and loss of another number.

# You are given an integer array nums representing the data status of this set after the error.

# Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

# Example 1:

# Input: nums = [1,2,2,4]
# Output: [2,3]
# Example 2:

# Input: nums = [1,1]
# Output: [1,2]
 

# Constraints:

# 2 <= nums.length <= 10**4
# 1 <= nums[i] <= 10**4

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        total_num=len(nums)

        count_list=[0]*(total_num+1)

        for i, num in enumerate(nums):
            count_list[num]+=1

        miss_num=-1
        dup_num=-1
        for i in range(1,total_num+1):
            if count_list[i]==0:
                miss_num=i
            elif count_list[i]==2:
                dup_num=i

        return [dup_num,miss_num]




