# LC00435_Non-overlapping_Intervals.py

# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

# Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

 

# Example 1:

# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
# Example 2:

# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
# Example 3:

# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

# Constraints:

# 1 <= intervals.length <= 10**5
# intervals[i].length == 2
# -5 * 10**4 <= starti < endi <= 5 * 10**4


#Idea: sort based on end, then take the first element as first element in result, 
# keep visiting, if start is smaller than previous result element's end, delete it.
#Complexity except sorting: O(N)
from typing import List
#from functools import cmp_to_key
# def cmp(element_x, element_y):
#     return element_x[1]-element_y[1]
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #intervals.sort(key=cmp_to_key(cmp))#less memory
        intervals.sort(key=lambda a: a[1])#faster
        result_last_element_end=intervals[0][1]
        count_delete=0
        for i in range(1, len(intervals)):
            if intervals[i][0]>=result_last_element_end:
                result_last_element_end=intervals[i][1]
            else:
                count_delete+=1
        return count_delete
            

        
