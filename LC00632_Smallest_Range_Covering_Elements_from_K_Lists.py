# LC00632_Smallest_Range_Covering_Elements_from_K_Lists.py

# You have k lists of sorted integers in non-decreasing order. 
# Find the smallest range that includes at least one number from each of the k lists.

# We define the range [a, b] is smaller than range [c, d] 
# if b - a < d - c or a < c if b - a == d - c.

 

# Example 1:

# Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
# Output: [20,24]
# Explanation: 
# List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
# List 2: [0, 9, 12, 20], 20 is in range [20,24].
# List 3: [5, 18, 22, 30], 22 is in range [20,24].
# Example 2:

# Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
# Output: [1,1]
 

# Constraints:

# nums.length == k
# 1 <= k <= 3500
# 1 <= nums[i].length <= 50
# -10**5 <= nums[i][j] <= 10**5
# nums[i] is sorted in non-decreasing order.

# Idea: first, merge all k lists into one list, (use heap of size k to track min )
# Inside that one list, also record the original list index. 
# Then, set left and right boundary. First set left=0, then search min right such 
# that [left, right] includes at least one element in each original list,
# then each time move left by one step, update right. 

from heapq import *

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        num_lists=len(nums)
        each_list_next_index=[1]*num_lists
        my_heap=[]
        for i in range(num_lists):
            heappush(my_heap,(nums[i][0],i))
        global_tuple_list=[]
        #merge lists
        while my_heap:
            cur_tuple=heappop(my_heap)
            value,list_ind=cur_tuple
            global_tuple_list.append(cur_tuple)
            if each_list_next_index[list_ind]<len(nums[list_ind]):
                heappush(my_heap,(nums[list_ind][each_list_next_index[list_ind]],list_ind))
            each_list_next_index[list_ind]+=1

        left=0
        bin_count=[0]*num_lists
        bin_count_zeros=num_lists
        right=-1
        while bin_count_zeros>0:
            right+=1
            value,list_ind=global_tuple_list[right]
            bin_count[list_ind]+=1
            if bin_count[list_ind]==1:
                bin_count_zeros-=1

        result=[global_tuple_list[left][0],global_tuple_list[right][0]]

        for left in range(1,len(global_tuple_list)):
            # look for next right

            # delete one element before cur left
            value,list_ind=global_tuple_list[left-1]
            bin_count[list_ind]-=1
            if bin_count[list_ind]==0:
                bin_count_zeros+=1

            while bin_count_zeros>0:
                right+=1
                if right>=len(global_tuple_list):
                    break
                value,list_ind=global_tuple_list[right]
                bin_count[list_ind]+=1
                if bin_count[list_ind]==1:
                    bin_count_zeros-=1
            if right>=len(global_tuple_list):
                break

            if global_tuple_list[right][0]-global_tuple_list[left][0]<result[1]-result[0]:
                result=[global_tuple_list[left][0],global_tuple_list[right][0]]

        return result





