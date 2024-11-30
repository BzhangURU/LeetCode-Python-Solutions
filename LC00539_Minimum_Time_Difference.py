# LC00539_Minimum_Time_Difference.py

# Given a list of 24-hour clock time points in "HH:MM" format, 
# return the minimum minutes difference between any two time-points in the list.
 

# Example 1:

# Input: timePoints = ["23:59","00:00"]
# Output: 1
# Example 2:

# Input: timePoints = ["00:00","23:59","00:00"]
# Output: 0
 

# Constraints:

# 2 <= timePoints.length <= 2 * 10^4
# timePoints[i] is in the format "HH:MM".

class Solution:
    def time_point_to_int(self, time_point):
        hour=int(time_point[0:2])
        minute=int(time_point[3:5])
        return hour*60+minute
    def findMinDifference(self, timePoints: List[str]) -> int:
        list_time=[0]*len(timePoints)
        for i in range(len(timePoints)):
            list_time[i]=self.time_point_to_int(timePoints[i])

        list_time.sort()
        dif=list_time[1]-list_time[0]
        if list_time[0]+24*60-list_time[-1]<dif:
            dif=list_time[0]+24*60-list_time[-1]
        for i in range(2,len(list_time)):
            if list_time[i]-list_time[i-1]<dif:
                dif=list_time[i]-list_time[i-1]
        
        return dif
