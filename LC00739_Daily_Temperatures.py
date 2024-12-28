# LC00739_Daily_Temperatures.py

# Given an array of integers temperatures represents the daily temperatures, 
# return an array answer such that answer[i] is the number of days you have 
# to wait after the ith day to get a warmer temperature. If there is no future 
# day for which this is possible, keep answer[i] == 0 instead.

 

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]
 

# Constraints:

# 1 <= temperatures.length <= 10**5
# 30 <= temperatures[i] <= 100

#Idea: monotonic stack

from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        my_stack=deque()

        for i in range(len(temperatures)):
            while my_stack:
                if temperatures[my_stack[-1]]<temperatures[i]:
                    ind=my_stack.pop()
                    result[ind]=i-ind
                else:
                    break
            my_stack.append(i)
        return result