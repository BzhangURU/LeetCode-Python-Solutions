# LC00795_Number_of_Subarrays_with_Bounded_Maximum.py

# Given an integer array nums and two integers left and right, return the number of 
# contiguous non-empty subarrays such that the value of the maximum array element in 
# that subarray is in the range [left, right].

# The test cases are generated so that the answer will fit in a 32-bit integer.

 

# Example 1:

# Input: nums = [2,1,4,3], left = 2, right = 3
# Output: 3
# Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
# Example 2:

# Input: nums = [2,9,2,5,6], left = 2, right = 8
# Output: 7
 

# Constraints:

# 1 <= nums.length <= 10**5
# 0 <= nums[i] <= 10**9
# 0 <= left <= right <= 10**9

# Idea: first, split list into sub-lists by seperating by nums higher than right. 
# then in sub-lists, use two-pointers search.

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        # first find longest subarrays without values higher than right
        i=0
        left_bound_index=-1
        right_bound_index=-1
        output=0
        while i<len(nums):
            if (i==0 and nums[i]<=right) or (i>0 and nums[i-1]>right and nums[i]<=right):
                left_bound_index=i
            if (i==len(nums)-1 and nums[i]<=right) or (i<len(nums)-1 and nums[i+1]>right and nums[i]<=right):
                right_bound_index=i
                #start two-points search. between [left_bound_index,right_bound_index]
                l_ind=left_bound_index
                r_ind=left_bound_index
                last_ind__with_value_equal_higher_than_left=l_ind-1
                for l_ind in range(left_bound_index,right_bound_index+1):
                    if last_ind__with_value_equal_higher_than_left<l_ind:
                        r_ind=l_ind
                        while nums[r_ind]<left:
                            r_ind+=1
                            if r_ind>right_bound_index:
                                break
                        last_ind__with_value_equal_higher_than_left=r_ind
                        if r_ind<=right_bound_index:
                            output+=right_bound_index-r_ind+1
                        else:
                            break
                    else:
                        output+=right_bound_index-r_ind+1
            i+=1
        return output
