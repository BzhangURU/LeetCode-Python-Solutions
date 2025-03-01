# LC00436_Find_Right_Interval.py

# You are given an array of intervals, where intervals[i] = [starti, endi] and each starti is unique.

# The right interval for an interval i is an interval j such that startj >= endi and startj is minimized. Note that i may equal j.

# Return an array of right interval indices for each interval i. If no right interval exists for interval i, then put -1 at index i.

 

# Example 1:

# Input: intervals = [[1,2]]
# Output: [-1]
# Explanation: There is only one interval in the collection, so it outputs -1.
# Example 2:

# Input: intervals = [[3,4],[2,3],[1,2]]
# Output: [-1,0,1]
# Explanation: There is no right interval for [3,4].
# The right interval for [2,3] is [3,4] since start0 = 3 is the smallest start that is >= end1 = 3.
# The right interval for [1,2] is [2,3] since start1 = 2 is the smallest start that is >= end2 = 2.
# Example 3:

# Input: intervals = [[1,4],[2,3],[3,4]]
# Output: [-1,2,-1]
# Explanation: There is no right interval for [1,4] and [3,4].
# The right interval for [2,3] is [3,4] since start2 = 3 is the smallest start that is >= end1 = 3.
 

# Constraints:

# 1 <= intervals.length <= 2 * 10**4
# intervals[i].length == 2
# -10**6 <= starti <= endi <= 10**6
# The start point of each interval is unique.

# Idea: first get list of indexes by sorting based on start, then get another list based on end
# then, iterate through list_end_based, find its right interval from list_start_based. 

from functools import cmp_to_key



class Solution:

    def compare_start(self,x,y):
        return self.intervals[x][0]-self.intervals[y][0]

    def compare_end(self,x,y):
        return self.intervals[x][1]-self.intervals[y][1]

    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        self.intervals=intervals
        total_num=len(intervals)
        list_range=[x for x in range(total_num)]

        list_end=sorted(list_range,key=cmp_to_key(self.compare_end))
        list_start=sorted(list_range,key=cmp_to_key(self.compare_start))
        result=[-1]*total_num

        j_start=0
        for i in range(total_num):
            while j_start<total_num and self.intervals[list_end[i]][1]>self.intervals[list_start[j_start]][0]:
                j_start+=1

        # then index i's right interval is j_start. (if j_start ==total_num, then -1)
            if j_start<total_num:
                result[list_end[i]]=list_start[j_start]
            else:
                result[list_end[i]]=-1
        return result

        


