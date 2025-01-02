# LC00491_Non-decreasing_Subsequences.py

# Given an integer array nums, return all the different possible non-decreasing 
# subsequences of the given array with at least two elements. You may return the answer in any order. 

# Example 1:

# Input: nums = [4,6,7,7]
# Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
# Example 2:

# Input: nums = [4,4,3,2,1]
# Output: [[4,4]]
 

# Constraints:

# 1 <= nums.length <= 15
# -100 <= nums[i] <= 100

#Idea: think about a sorted array, then all subsequences with at least two elements will be qualified,
# So we print lists in same order, but check if it is non-decreasing. 
#But I got wrong results because of duplication:
# nums =
# [4,6,7,7]
# Output
# [[4,6],[4,6,7],[4,6,7,7],[4,6,7],[4,6],[4,6,7],[4,6],[4,7],[4,7,7],[4,7],[4,7],[6,7],[6,7,7],[6,7],[6,7],[7,7]]
# Expected
# [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
# So, one idea is that, after the last element in current list, if you have abandoned a number, you are not allowed to 
# take that number again in following part. We use a set to do it. 

from typing import List
class Solution:
    def outputSubsequences(self, nums, cur_list, next_ind, result, my_set):
        # we can't put it here, otherwise we skip a new element and output the same cur_list again!!!
        # if len(cur_list)>=2:
        #     one_result=cur_list.copy()
        #     result.append(one_result)

        if next_ind==len(nums) or (next_ind==len(nums)-1 and len(cur_list)==0):
            return 
        
        if (len(cur_list)==0 or cur_list[-1]<=nums[next_ind]) and (nums[next_ind] not in my_set):
            cur_list.append(nums[next_ind])
            #cur_list.append(next_ind)
            if len(cur_list)>=2:
                one_result=cur_list.copy()
                result.append(one_result)
            new_set=set()
            self.outputSubsequences(nums, cur_list,next_ind+1,result, new_set)
            cur_list.pop()
        
        #we skip the next_ind
        extra_element_added_in_set=False
        # "and nums[next_ind] not in my_set" is important, otherwise we could already have 7 in set, 
        # then in second 7, we add 7 again in set (void), and remove the first 7!!!
        if (len(cur_list)==0 or cur_list[-1]<=nums[next_ind]) and (nums[next_ind] not in my_set):
            my_set.add(nums[next_ind])
            extra_element_added_in_set=True
        self.outputSubsequences(nums, cur_list,next_ind+1,result, my_set)
        if extra_element_added_in_set:
            my_set.remove(nums[next_ind])

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result=[]
        cur_list=[]
        my_set=set()
        self.outputSubsequences(nums,cur_list,0,result, my_set)
        return result

my_solu=Solution()
nums=[4,6,7,7]
result=my_solu.findSubsequences(nums)
print(result)
        
