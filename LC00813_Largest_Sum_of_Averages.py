# LC00813_Largest_Sum_of_Averages.py

# You are given an integer array nums and an integer k. 
# You can partition the array into at most k non-empty adjacent subarrays. 
# The score of a partition is the sum of the averages of each subarray.

# Note that the partition must use every integer in nums, and that the score is not necessarily an integer.

# Return the maximum score you can achieve of all the possible partitions. 
# Answers within 10-6 of the actual answer will be accepted.

 

# Example 1:

# Input: nums = [9,1,2,3,9], k = 3
# Output: 20.00000
# Explanation: 
# The best choice is to partition nums into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
# We could have also partitioned nums into [9, 1], [2], [3, 9], for example.
# That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.
# Example 2:

# Input: nums = [1,2,3,4,5,6,7], k = 4
# Output: 20.50000
 

# Constraints:

# 1 <= nums.length <= 100
# 1 <= nums[i] <= 10**4
# 1 <= k <= nums.length


from typing import List
class Solution:
    def my_largest_sum_of_avg(self,nums,cumulative_sum,my_dict,k,left,right):
        if k==1:
            return (cumulative_sum[right]-cumulative_sum[left-1])/(right-left+1)
            # if left>0:
            #     return cumulative_sum[right]-cumulative_sum[left-1]
            # else:
            #     return cumulative_sum[right]
        else:
            if (k,left,right) in my_dict:
                return my_dict[(k,left,right)]
            else:
                largest_sum_avg=0.0
                for middle in range(left,right-(k-1)+1):
                    #left-middle middle+1----right
                    cur_avg=(cumulative_sum[middle]-cumulative_sum[left-1])/(middle-left+1)
                    sum_of_avg=cur_avg+self.my_largest_sum_of_avg(nums,cumulative_sum,my_dict,k-1,middle+1,right)
                    if sum_of_avg>largest_sum_avg:
                        largest_sum_avg=sum_of_avg
                my_dict[(k,left,right)]=largest_sum_avg
                return largest_sum_avg


    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        cumulative_sum=[float(nums[0])]*len(nums)
        for i in range(1,len(nums)):
            cumulative_sum[i]=cumulative_sum[i-1]+float(nums[i])
        cumulative_sum.append(0.0)

        my_dict={}

        return self.my_largest_sum_of_avg(nums,cumulative_sum,my_dict,k,0,len(nums)-1)
        

nums=[9,1,2,3,9]
my_solu=Solution()
print(my_solu.largestSumOfAverages(nums,3))
