# LC00659_Split_Array_into_Consecutive_Subsequences.py

# You are given an integer array nums that is sorted in non-decreasing order.

# Determine if it is possible to split nums into one or more subsequences such that 
# both of the following conditions are true:

# Each subsequence is a consecutive increasing sequence (i.e. each integer is exactly 
#                                                        one more than the previous integer).
# All subsequences have a length of 3 or more.
# Return true if you can split nums according to the above conditions, or false otherwise.

# A subsequence of an array is a new array that is formed from the original array 
# by deleting some (can be none) of the elements without disturbing the relative 
# positions of the remaining elements. (i.e., [1,3,5] is a subsequence of 
#                                       [1,2,3,4,5] while [1,3,2] is not).

 

# Example 1:

# Input: nums = [1,2,3,3,4,5]
# Output: true
# Explanation: nums can be split into the following subsequences:
# [1,2,3,3,4,5] --> 1, 2, 3
# [1,2,3,3,4,5] --> 3, 4, 5
# Example 2:

# Input: nums = [1,2,3,3,4,4,5,5]
# Output: true
# Explanation: nums can be split into the following subsequences:
# [1,2,3,3,4,4,5,5] --> 1, 2, 3, 4, 5
# [1,2,3,3,4,4,5,5] --> 3, 4, 5
# Example 3:

# Input: nums = [1,2,3,4,4,5]
# Output: false
# Explanation: It is impossible to split nums into consecutive increasing 
# subsequences of length 3 or more.
 

# Constraints:

# 1 <= nums.length <= 10**4
# -1000 <= nums[i] <= 1000
# nums is sorted in non-decreasing order.

# Idea: count each number's occurence to get bin. Then, start from smallest number to start subsequences
# If next number's count is larger than previous one, then start new subsequences
# If next number's count is smaller than previous one, then end some of current subsequences by ending earliest start subseq first.

from collections import deque

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        my_q=deque()# save current subseqs' start num
        unique_nums=[]

        my_dict_count={}
        for i in range(0, len(nums)):
            if nums[i] not in my_dict_count:
                my_dict_count[nums[i]]=1
            else:
                my_dict_count[nums[i]]+=1

        for i in range(0,len(nums)):
            if len(unique_nums)==0 or unique_nums[-1]!=nums[i]:
                unique_nums.append(nums[i])

        min_num_count=my_dict_count[nums[0]]
        for i in range(min_num_count):
            my_q.append(nums[0])
            
        cur_subseq_count=min_num_count

        for i in range(1, len(unique_nums)):
            cur_num=unique_nums[i]
            cur_num_count=my_dict_count[cur_num]

            if cur_num>unique_nums[i-1]+1:
                #there is a gap, all existing subseq needs to end
                while my_q:
                    start_num=my_q.popleft()
                    if unique_nums[i-1] - start_num<2:
                        return False
                #start new subseqs, put them to my_heap
                for j in range(cur_num_count):
                    my_q.append(cur_num)

            else:
                # no gap, compare count
                prev_num_count=my_dict_count[unique_nums[i-1]]
                if prev_num_count<cur_num_count:
                    additional_num=cur_num_count-prev_num_count
                    for j in range(additional_num):
                        my_q.append(cur_num)
                else:
                    decreased_num=prev_num_count-cur_num_count
                    for j in range(decreased_num):
                        start_num=my_q.popleft()
                        if unique_nums[i-1] - start_num<2:
                            return False
                        
        while my_q:
            start_num=my_q.popleft()
            if unique_nums[-1] - start_num<2:
                return False
            
        return True

                



        
            



        

        
        

        
        


