# LC00630_Course_Schedule_III.py

# There are n different online courses numbered from 1 to n. You are given an array courses where 
# courses[i] = [durationi, lastDayi] indicate that the ith course should be taken continuously 
# for durationi days and must be finished before or on lastDayi.

# You will start on the 1st day and you cannot take two or more courses simultaneously.

# Return the maximum number of courses that you can take.

 

# Example 1:

# Input: courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
# Output: 3
# Explanation: 
# There are totally 4 courses, but you can take 3 courses at most:
# First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready 
# to take the next course on the 101st day.
# Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, 
# and ready to take the next course on the 1101st day. 
# Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day. 
# The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.
# Example 2:

# Input: courses = [[1,2]]
# Output: 1
# Example 3:

# Input: courses = [[3,2],[4,3]]
# Output: 0
 

# Constraints:

# 1 <= courses.length <= 10**4
# 1 <= durationi, lastDayi <= 10**4

#Hint:
# During iteration, say I want to add the current course, currentTotalTime being total time of all 
# courses taken till now, but adding the current course might exceed my deadline or it doesn’t.

# 1. If it doesn’t, then I have added one new course. Increment the currentTotalTime 
# with duration of current course.

# 2. If it exceeds deadline, I can swap current course with current courses that has biggest duration.
# * No harm done and I might have just reduced the currentTotalTime, right?
# * What preprocessing do I need to do on my course processing order so that this swap is always legal?

# Idea: First sort courses based on lastDay, then iterate to add courses, 
# during iteration, record currrent total duration (you are able to finished all previous courses before 
# currrent total duration, by taking courses back to back). If cur_total_duration + duration_i < lastDay_i, 
# then add this course, otherwise get the longest course (including i) and remove it. 

from heapq import *

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        my_heap=[]
        courses.sort(key=lambda p: p[1])
        prev_total_duration=0
        result=0

        for i in range(len(courses)):
            if prev_total_duration+courses[i][0]<=courses[i][1]:
                heappush(my_heap,(-courses[i][0],i))
                prev_total_duration+=courses[i][0]
                result+=1
            else:
                if prev_total_duration==0 or courses[i][0]>-my_heap[0][0]:
                    pass
                else:
                    removed_course=heappop(my_heap)
                    prev_total_duration-=courses[removed_course[1]][0]
                    heappush(my_heap,(-courses[i][0],i))
                    prev_total_duration+=courses[i][0]
        return result
                    

        
