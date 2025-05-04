# LC00698_Partition_to_K_Equal_Sum_Subsets.py

# Given an integer array nums and an integer k, return true if it is possible to 
# divide this array into k non-empty subsets whose sums are all equal.

 

# Example 1:

# Input: nums = [4,3,2,3,5,2,1], k = 4
# Output: true
# Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
# Example 2:

# Input: nums = [1,2,3,4], k = 3
# Output: false
 

# Constraints:

# 1 <= k <= nums.length <= 16
# 1 <= nums[i] <= 10**4
# The frequency of each element is in the range [1, 4].

from typing import List

# Idea: brute force, sort, start from larest numbers first, use k bins to save current sum, 
# if some bins have same current sum, then just try assigning current value to last of them. 
# if nums have some same values, then if current num is put into bin m, then the next num (with same value)
# will only go to bin m, m+1, ..., k
# if answer is already found, stop

class Solution:
    def iterate_nums(self,nums,goal,k,bins,num_ind,last_chosen_bin_ind):
        if bins==[3,3,4,5]:
            bins[0]=bins[0]
        if bins[0]==3:
            bins[0]=bins[0]

        if num_ind==len(nums):
            for i in range(k):
                if bins[i]!=goal:
                    return False
            return True
        else:
            for i in range(k):
                skip_this=False
                if num_ind>0 and nums[num_ind-1]==nums[num_ind] and last_chosen_bin_ind>i:
                    skip_this=True
                if skip_this==False:
                    #for j in range(i+1,k):#this is wrong
                    for j in range(i):
                        if bins[i]==bins[j]:
                            skip_this=True
                            break
                if skip_this:
                    continue
                if bins[i]+nums[num_ind]<=goal:
                    bins[i]+=nums[num_ind]
                    answer=self.iterate_nums(nums,goal,k,bins,num_ind+1,i)
                    if answer:
                        return True
                    bins[i]-=nums[num_ind]
            return False
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        bins=[0]*k
        total_sum=sum(nums)
        if total_sum%k!=0:
            return False
        goal=total_sum//k
        if goal==0:
            return False
        nums.sort(reverse=True)
        result=self.iterate_nums(nums,goal,k,bins,0,-1)
        return result
        
my_solu=Solution()
nums=[4,3,2,3,5,2,1]
print(my_solu.canPartitionKSubsets(nums,4))
        
        
        
