#LC00743_Network_Delay_Time

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

#idea: breadth first search. If shorter time is found, update it. 

from collections import deque

class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        if len(times)<n-1:
            return -1
        
        edges={}
        node_delay_time=[-1]*(n+1)
        node_delay_time[k]=0
        for edge in times:
            if edge[0] not in edges:
                edges[edge[0]]={edge[1]:edge[2]}
            else:
                edges[edge[0]][edge[1]]=edge[2]
                
                
        node_queue=deque()
        node_queue.append(k)
        
        while node_queue:
            queue_len=len(node_queue)
            for i in range(queue_len):
                cur_node=node_queue.popleft()
                if cur_node in edges:
                    for adj_node in edges[cur_node]:
                        if node_delay_time[adj_node]<0 or node_delay_time[adj_node]>node_delay_time[cur_node]+edges[cur_node][adj_node]:
                            node_delay_time[adj_node]=node_delay_time[cur_node]+edges[cur_node][adj_node]
                            node_queue.append(adj_node)
            
        result=-1
        for i in range(1,n+1):
            if node_delay_time[i]==-1:
                return -1
            if node_delay_time[i]>result or result==-1:
                result=node_delay_time[i]
        return result
