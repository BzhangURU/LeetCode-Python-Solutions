#LC00743_Network_Delay_Time__heapq.py

# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as 
# directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time 
# it takes for a signal to travel from source to target.

# We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the 
# signal. If it is impossible for all the n nodes to receive the signal, return -1.

 

# Example 1:


# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2
# Example 2:

# Input: times = [[1,2,1]], n = 2, k = 1
# Output: 1
# Example 3:

# Input: times = [[1,2,1]], n = 2, k = 2
# Output: -1
 

# Constraints:

# 1 <= k <= n <= 100
# 1 <= times.length <= 6000
# times[i].length == 3
# 1 <= ui, vi <= n
# ui != vi
# 0 <= wi <= 100
# All the pairs (ui, vi) are unique. (i.e., no multiple edges.)

# new idea: use heapq. The challenging part is that a node could be reached by multiple paths. 
# (one path takes 8 steps with delay time 100, another path takes 10 steps with delay time 90. )
# The BFS (or DFS) need to recheck and maybe restart from the new path and explore again. 
# But the heapq always pop the node with minimum delay time, so no other path can take shorter time than it.
# The only trouble is that, imagine we pop one node, and then we push that node's neighbor with delay time to heapq,
# but that new neighbor node may already exist in the heapq, and the delay time is probably different. So how can we
# quickly update the new neighbor node? (replace old one?) 
# Actually we don't need to replace, we just need a dict or array to record the minimum delay time for that node,
# then when we pop out a node from heapq, we compare it with the dict/array. Discard it if the recorded delay time in heapq
# is larger than in dict/array. As a result, we don't need to replace the old one. The old one is OK to keep staying in heapq.  
#   
# first put k into heap, then pop it out, save its neighbors into heapq. Continue to pop the min one. 
# 
# This algorithm is actually the Dijkstra algorithm




from heapq import *

class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        minDelayTime=[-1]*(n+1)
        nodeDict={}
        for edge in times:
            if edge[0] not in nodeDict:
                nodeDict[edge[0]]={}
            nodeDict[edge[0]][edge[1]]=edge[2]

        hq=[]
        heappush(hq,(0,k))

        while len(hq)>0:
            delayTime, node=heappop(hq)
            if minDelayTime[node]<0:
                minDelayTime[node]=delayTime
                if node in nodeDict:
                    for nextNode, Dif in nodeDict[node].items():
                        heappush(hq,(delayTime+Dif,nextNode))

        minDelayTime[0]=0#can't set to 1000 because we are getting max(minDelayTime) 
        if minDelayTime.count(-1)>0:#can't use .index, will return error if not exist
            return -1
        else:
            return max(minDelayTime) 
