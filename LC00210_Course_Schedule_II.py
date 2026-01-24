# LC00210_Course_Schedule_II.py

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must 
# take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, 
# return any of them. If it is impossible to finish all courses, return an empty array.

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. 
# So the correct course order is [0,1].
# Example 2:

# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should 
# have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
# Example 3:

# Input: numCourses = 1, prerequisites = []
# Output: [0]
 

# Constraints:

# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= numCourses * (numCourses - 1)
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# ai != bi
# All the pairs [ai, bi] are distinct.


# Idea: First, define dictionary that saves pre-requisites of each courses. 
# Also define dictionary descendants that saves descendants of each courses.
# Attention: each course may have multiple prerequisites or descendants.

# we use BFS, we first find courses that have no prerequisites, if they don't exist, then we return [],
# otherwise, we put them to output array, as well as a set called visitedCourses. 
# In second step, we find courses that have no prerequisites IF visitedCourses are ignored. we put them to output array, 
# as well as into set. 
# The third step is same as second step......

# To save time in running code, in second (and later) steps, we only find courses that belong to descendants of previously
# just found courses. 

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dictPrereq={}
        dictDescend={}
        for myPair in prerequisites:
            if myPair[0] not in dictPrereq:
                dictPrereq[myPair[0]]=set([myPair[1]])
            else:
                dictPrereq[myPair[0]].add(myPair[1])
            if myPair[1] not in dictDescend:
                dictDescend[myPair[1]]=set([myPair[0]])
            else:
                dictDescend[myPair[1]].add(myPair[0])

        output=[]
        visitedCourses=set()

        visitingCourses=set()
        for i in range(numCourses):
            if i not in dictPrereq:
                visitingCourses.add(i)
        if len(visitingCourses)==0:
            return []
        
            
        
        
        while len(visitingCourses)>0:
            for c in visitingCourses:
                output.append(c)
                visitedCourses.add(c)

            newCoursesCandidates=set()#only courses in newCoursesCandidates MAY be new visitingCourses
            for course in visitingCourses:
                if course in dictDescend:
                    newCoursesCandidates.update(dictDescend[course])

            visitingCourses.clear()
            for course in newCoursesCandidates:
                qualified=True
                for pre in dictPrereq[course]:
                    if pre not in visitedCourses:
                        qualified=False
                        break
                if qualified:
                    visitingCourses.add(course)
            newCoursesCandidates.clear()

        if len(output)<numCourses:
            return []
        else:
            return output
