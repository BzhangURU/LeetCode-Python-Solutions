# LC00740_Delete_and_Earn.py

# You are given an integer array nums. You want to maximize the number of points you get 
# by performing the following operation any number of times:

# Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every 
# element equal to nums[i] - 1 and every element equal to nums[i] + 1.
# Return the maximum number of points you can earn by applying the above operation some number of times.

 

# Example 1:

# Input: nums = [3,4,2]
# Output: 6
# Explanation: You can perform the following operations:
# - Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
# - Delete 2 to earn 2 points. nums = [].
# You earn a total of 6 points.
# Example 2:

# Input: nums = [2,2,3,3,3,4]
# Output: 9
# Explanation: You can perform the following operations:
# - Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
# - Delete a 3 again to earn 3 points. nums = [3].
# - Delete a 3 once more to earn 3 points. nums = [].
# You earn a total of 9 points.
 

# Constraints:

# 1 <= nums.length <= 2 * 10**4
# 1 <= nums[i] <= 10**4

# Idea: DP. Change [2,2,3,3,3,4] to nums_frequency: [[2,2],[3,3],[4,1]]
from typing import List
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        nums_frequency=[[nums[0],1]]

        for i in range(1,len(nums)):
            if nums[i]==nums_frequency[-1][0]:
                nums_frequency[-1][1]+=1
            else:
                nums_frequency.append([nums[i],1])
        if len(nums_frequency)==1:
            return nums_frequency[0][0]*nums_frequency[0][1]
        
        DP=[-1]*len(nums_frequency)
        #DP[i] means the last deleted num is index i

        DP[0]=nums_frequency[0][0]*nums_frequency[0][1]
        if nums_frequency[1][0]==nums_frequency[0][0]+1:
            DP[1]=nums_frequency[1][0]*nums_frequency[1][1]
        else:
            DP[1]=nums_frequency[1][0]*nums_frequency[1][1]+nums_frequency[0][0]*nums_frequency[0][1]

        get_max_DP_until=[0]*len(nums_frequency)
        get_max_DP_until[0]=DP[0]
        get_max_DP_until[1]=max(DP[0],DP[1])

        for i in range(2,len(nums_frequency)):
            if nums_frequency[i][0]==nums_frequency[i-1][0]+1:
                DP[i]=get_max_DP_until[i-2]+nums_frequency[i][0]*nums_frequency[i][1]
                get_max_DP_until[i]=max(DP[i],get_max_DP_until[i-1])
            else:
                DP[i]=get_max_DP_until[i-1]+nums_frequency[i][0]*nums_frequency[i][1]
                get_max_DP_until[i]=DP[i]
        return get_max_DP_until[len(nums_frequency)-1]

my_solu=Solution()
nums = [2,2,3,3,3,4]
my_solu.deleteAndEarn(nums)




        

