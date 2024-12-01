# LC00540_Single_Element_in_a_Sorted_Array.py

# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

# Return the single element that appears only once.

# Your solution must run in O(log n) time and O(1) space.

 

# Example 1:

# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:

# Input: nums = [3,3,7,7,10,11,11]
# Output: 10
 

# Constraints:

# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^5

#Idea: use bisection method to find it

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        if len(nums)==1:
            return nums[0]

        left=0
        right=len(nums)-2


        if nums[left]!=nums[left+1]:
            return nums[left]
        if nums[right]!=nums[right+1]:
            return nums[right+1]

        #nums[left]== nums[left+1] (left is always even number)
        #nums[right]== nums[right+1] (right is always odd number)
        #finally we will reach sth like left==10, right==13, then output nums[12]
        while left<right-3:
            
            middle=(left+right)//2
            middle=middle-(middle%2)

            if nums[middle]==nums[middle+1]:
                left=middle
            else:
                right=middle+1
        return nums[right-1]
