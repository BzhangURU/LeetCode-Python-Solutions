# LC00621_Task_Scheduler_faster.py

# You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. 
# Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in 
# any order, but there's a constraint: there has to be a gap of at least n intervals between 
# two tasks with the same label.

# Return the minimum number of CPU intervals required to complete all tasks.

 

# Example 1:

# Input: tasks = ["A","A","A","B","B","B"], n = 2

# Output: 8

# Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

# After completing task A, you must wait two intervals before doing A again. The same applies to task B. 
# In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, 
# you can do A again as 2 intervals have passed.

# Example 2:

# Input: tasks = ["A","C","A","B","D","B"], n = 1

# Output: 6

# Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

# With a cooling interval of 1, you can repeat a task after just one other task.

# Example 3:

# Input: tasks = ["A","A","A", "B","B","B"], n = 3

# Output: 10

# Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

# There are only two types of tasks, A and B, which need to be separated by 3 intervals. 
# This leads to idling twice between repetitions of these tasks.

 

# Constraints:

# 1 <= tasks.length <= 104
# tasks[i] is an uppercase English letter.
# 0 <= n <= 100

# Idea: if n=4, and the ABCDE's tasks count are 10,8,7,6,5, then we can directly reduce to 5,3,2,1,0 without waiting.
# If the tasks count is 10,8,7,6,5, 3,3,2, then we can use(3+3+2) to add to 5,3,2,1, to make min of (5,3,2,1) as large as possible
from typing import List
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        raw_count_each_letter_tasks=[0]*26
        for i in range(len(tasks)):
            raw_count_each_letter_tasks[ord(tasks[i])-ord('A')]+=1
        # change 0,0,2,3,0,4,0,0,2,... to 2,3,4,2,0,4,0,0,2,... and count_letters will be 4(valid count)
        count_each_letter_tasks=[]
        for i in range(26):
            if raw_count_each_letter_tasks[i]>0:
                count_each_letter_tasks.append(raw_count_each_letter_tasks[i])
        count_each_letter_tasks.sort()
        count_each_letter_tasks.reverse()

        cancel_out_waiting_time=0
        if len(count_each_letter_tasks)>n+1:
            #count (3+3+2), that will cancel out same waiting time
            for i in range(n+1,len(count_each_letter_tasks)):
                cancel_out_waiting_time+=count_each_letter_tasks[i]
        

        # if n=4, original tasks count are 10,8,7, then the result would be same as 10,9,9,9,9
        count_same_max=0
        max_num=max(count_each_letter_tasks)

        ind_end=min(n+1,len(count_each_letter_tasks))

        for i in range(0,ind_end):
            if count_each_letter_tasks[i]==max_num:
                count_same_max+=1
        
        first_n_plus_one_result=(max_num-1)*(n+1)+count_same_max
        # print('max_num',max_num)
        # print('count_same_max',count_same_max)
        # print('first_n_plus_one_result',first_n_plus_one_result)
        sum_first_n_plus_one=0
        for i in range(0,ind_end):
            sum_first_n_plus_one+=count_each_letter_tasks[i]
        # print('sum_first_n_plus_one',sum_first_n_plus_one)

        #if there is only first n+1 letters or less letters, the original total waiting time
        original_total_waiting_time=first_n_plus_one_result-sum_first_n_plus_one
        total_extra_time=max(original_total_waiting_time,cancel_out_waiting_time)
        # print('original_total_waiting_time',original_total_waiting_time)
        # print('cancel_out_waiting_time',cancel_out_waiting_time)
        # print('total_extra_time',total_extra_time)
        result=sum_first_n_plus_one+total_extra_time
        return result
