# LC00719_Find_K-th_Smallest_Pair_Distance.py

# The distance of a pair of integers a and b is defined as the absolute difference between a and b.

# Given an integer array nums and an integer k, return the kth smallest distance among all 
# the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

 

# Example 1:

# Input: nums = [1,3,1], k = 1
# Output: 0
# Explanation: Here are all the pairs:
# (1,3) -> 2
# (1,1) -> 0
# (3,1) -> 2
# Then the 1st smallest distance pair is (1,1), and its distance is 0.
# Example 2:

# Input: nums = [1,1,1], k = 2
# Output: 0
# Example 3:

# Input: nums = [1,6,1], k = 3
# Output: 5
 

# Constraints:

# n == nums.length
# 2 <= n <= 10**4
# 0 <= nums[i] <= 10**6
# 1 <= k <= n * (n - 1) / 2


#Hint: Binary search for the answer. How can you check how many pairs have distance <= X?

#Keys: don't double the count of pairs, (i,j) and (j,i) are same pair. 


from typing import List

class Solution:
    def countPairsWithDistanceLowerEqualX(self, sortedNums, x):
        output=0
        for i, num in enumerate(sortedNums):
            #search either before num and after num

            # before num: find smallest index before num that num-sortedNums[target]<=x
            countBeforeNum=0
            if i>0:
                if num-sortedNums[i-1]>x:
                    countBeforeNum=0
                elif num-sortedNums[0]<=x:
                    countBeforeNum=i
                else:
                    left=0
                    right=i-1
                    while left+1<right:
                        middle=(left+right)//2
                        if num-sortedNums[middle]<=x:
                            right=middle
                        else:
                            left=middle
                    #right is the target
                    countBeforeNum=i-right
            output+=countBeforeNum
        return output


    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        #we need to find low and high distance boundary (finally low+1==high), countPairs(low)<k, countPairs(high)>=k, then output is high.
        high=nums[-1]-nums[0]+1
        low=0

        if self.countPairsWithDistanceLowerEqualX(nums,low)>=k:
            return low
        else:
            while low+1<high:
                middle=(low+high)//2
                if self.countPairsWithDistanceLowerEqualX(nums,middle)<k:
                    low=middle
                else:
                    high=middle
        return high
