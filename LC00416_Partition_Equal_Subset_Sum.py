# LC00416_Partition_Equal_Subset_Sum.py

# Given an integer array nums, return true if you can partition the array 
# into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

# Example 1:

# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:

# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
 

# Constraints:

# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100

# Idea: imagine we there is an array, we get a set of possible subset sum, then we add a new element to 
# array, we need to update the set by adding (original element + new element value) to the set. 

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum=sum(nums)
        if total_sum%2!=0:
            return False
        goal=total_sum//2

        set_possible_subset_sum=set()
        set_possible_subset_sum.add(0)
        set_possible_subset_sum.add(nums[0])
        if goal==0 or goal==nums[0]:
            return True

        for i in range(1,len(nums)):
            num=nums[i]

            set_temp_for_new_element=set()

            for element in set_possible_subset_sum:
                if element+num==goal:
                    return True
                if (element+num) not in set_possible_subset_sum and \
                    (element+num) not in set_temp_for_new_element:
                    set_temp_for_new_element.add(element+num)
            set_possible_subset_sum=set_possible_subset_sum | set_temp_for_new_element
        return False

            
