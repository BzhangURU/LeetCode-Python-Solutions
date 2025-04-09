# LC00672_Bulb_Switcher_II.py

# There is a room with n bulbs labeled from 1 to n that all are turned on initially, and four 
# buttons on the wall. Each of the four buttons has a different functionality where:

# Button 1: Flips the status of all the bulbs.
# Button 2: Flips the status of all the bulbs with even labels (i.e., 2, 4, ...).
# Button 3: Flips the status of all the bulbs with odd labels (i.e., 1, 3, ...).
# Button 4: Flips the status of all the bulbs with a label j = 3k + 1 where k = 0, 1, 2, ... (i.e., 1, 4, 7, 10, ...).
# You must make exactly presses button presses in total. For each press, you may pick any of the four buttons to press.

# Given the two integers n and presses, return the number of different possible statuses 
# after performing all presses button presses.

 

# Example 1:

# Input: n = 1, presses = 1
# Output: 2
# Explanation: Status can be:
# - [off] by pressing button 1
# - [on] by pressing button 2
# Example 2:

# Input: n = 2, presses = 1
# Output: 3
# Explanation: Status can be:
# - [off, off] by pressing button 1
# - [on, off] by pressing button 2
# - [off, on] by pressing button 3
# Example 3:

# Input: n = 3, presses = 1
# Output: 4
# Explanation: Status can be:
# - [off, off, off] by pressing button 1
# - [off, on, off] by pressing button 2
# - [on, off, on] by pressing button 3
# - [off, on, on] by pressing button 4
 

# Constraints:

# 1 <= n <= 1000
# 0 <= presses <= 1000

# Idea: The period is 6 (1 and 7 always have same status). So first reduce num bulbs to min(n, 6)

class Solution:
    def oper1(self,one_status_list):
        for i in range(len(one_status_list)):
            one_status_list[i]=1-one_status_list[i]

    def oper2(self,one_status_list):
        for i in range(len(one_status_list)):
            if i&1==1:
                one_status_list[i]=1-one_status_list[i]

    def oper3(self,one_status_list):
        for i in range(len(one_status_list)):
            if i&1==0:
                one_status_list[i]=1-one_status_list[i]

    def oper4(self,one_status_list):
        for i in range(len(one_status_list)):
            if i%3==0:
                one_status_list[i]=1-one_status_list[i]

    def flipLights(self, n: int, presses: int) -> int:
        n=min(n,6)
        status=[1 for i in range(n)]

        status_set=set()
        status_set.add(tuple(status))

        for i in range(presses):
            new_status_set=set()
            for one_status in status_set:
                # traverse 4 operations
                one_status_list=list(one_status)
                self.oper1(one_status_list)
                new_status_set.add(tuple(one_status_list))

                one_status_list=list(one_status)
                self.oper2(one_status_list)
                new_status_set.add(tuple(one_status_list))
                
                one_status_list=list(one_status)
                self.oper3(one_status_list)
                new_status_set.add(tuple(one_status_list))

                one_status_list=list(one_status)
                self.oper4(one_status_list)
                new_status_set.add(tuple(one_status_list))

            status_set=new_status_set
            if (presses-1-i)&1==0 and len(status_set)==64:
                # we can easily keep doing oper1 to have same max num of status, so skip following operations. 
                break
        return len(status_set)
                


        
