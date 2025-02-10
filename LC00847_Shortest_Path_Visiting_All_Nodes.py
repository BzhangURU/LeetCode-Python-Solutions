# LC00847_Shortest_Path_Visiting_All_Nodes.py

# You have an undirected, connected graph of n nodes labeled from 0 to n - 1. 
# You are given an array graph where graph[i] is a list of all the nodes 
# connected with node i by an edge.

# Return the length of the shortest path that visits every node. You may start 
# and stop at any node, you may revisit nodes multiple times, and you may reuse 
# edges.

# Existing idea: use BFS, each "node" is defined as (set of visited numbers, last number visited)
# the depth of node is distance of path so far. If set of visited numbers is all, then we stop. 
# we allow to visit already visited numbers, but we don't allow to visit already visited (set of visited numbers, last number visited)

from typing import List
from collections import deque


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        set_visited_path=set()

        n=len(graph)

        #binary mask saves set of visited numbers
        goal_binary_mask=2**n-1
        my_q=deque()

        for i in range(n):
            mask=1<<i
            my_q.append((mask,i))
            set_visited_path.add((mask,i))
            if mask==goal_binary_mask:
                return 0

        path=0

        while my_q:
            length_q=len(my_q)
            path+=1
            for i in range(length_q):
                
                mask,cur_num=my_q.popleft()
                #look for next number

                for next_num in graph[cur_num]:
                    new_mask=mask | (1<<next_num)
                    if (new_mask,next_num) not in set_visited_path:
                        my_q.append((new_mask,next_num))
                        set_visited_path.add((new_mask,next_num))
                        if new_mask==goal_binary_mask:
                            return path
        return path





        

        
#graph=[[1,2,3],[0],[0],[0]]
#graph=[[1],[0,2,4],[1,3,4],[2],[1,2]]
graph=[[2,3,6],[5],[0,3],[0,2,4,7],[3],[7,1],[0],[3,5]]
my_solu=Solution()
print(my_solu.shortestPathLength(graph))





