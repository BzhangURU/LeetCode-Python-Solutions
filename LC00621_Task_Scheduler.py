# LC00621_Task_Scheduler.py

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

# Idea: if currently there are tasks that doesn't need idling, do them first. In those tasks,
# do the one that counts most. If all tasks still needs idling, wait. 
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
        idling_times=[0]*len(count_each_letter_tasks)
        result=0
        while count_each_letter_tasks:
            min_idling_time=min(idling_times)
            if min_idling_time==0:
                # print('Process')
                # print(count_each_letter_tasks)
                # print(idling_times)
                #find indices where idling_time is 0, then find the max count
                target_ind=idling_times.index(0)
                for i in range(len(count_each_letter_tasks)):
                    if idling_times[i]==0:
                        if count_each_letter_tasks[i]>count_each_letter_tasks[target_ind]:
                            target_ind=i
                result+=1
                for i in range(len(idling_times)):
                    if idling_times[i]>0:
                        idling_times[i]-=1
                if count_each_letter_tasks[target_ind]>1:
                    count_each_letter_tasks[target_ind]-=1
                    idling_times[target_ind]=n
                else:
                    del count_each_letter_tasks[target_ind]
                    del idling_times[target_ind]
                # print(count_each_letter_tasks)
                # print(idling_times)
                # print('\n')
            else:
                result+=min_idling_time
                for i in range(len(count_each_letter_tasks)):
                    idling_times[i]-=min_idling_time
                # print('wait')
                # print(count_each_letter_tasks)
                # print(idling_times)
                # print('\n')
        # print(result)
        return result
