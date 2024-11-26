# LC00834_Sum_of_Distance_in_Tree_shorter_processing_time.py

# There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

# You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

# Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.

 

# Example 1:


# Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
# Output: [8,12,6,10,10,10]
# Explanation: The tree is shown above.
# We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
# equals 1 + 1 + 2 + 2 + 2 = 8.
# Hence, answer[0] = 8, and so on.
# Example 2:


# Input: n = 1, edges = []
# Output: [0]
# Example 3:


# Input: n = 2, edges = [[1,0]]
# Output: [1,1]
 

# Constraints:

# 1 <= n <= 3 * 10^4
# edges.length == n - 1
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# The given input represents a valid tree.


# Idea: Let 0 to be the root to calculate answer[0]. Breadth-first search tree, save depth of each node, (0 is depth 0). 
# After getting dis(0,j), add it to answer[0]
# Another idea is: if i is parent of j, then answer[j]=answer[i]+number of nodes closer to i  - number of nodes closer to j
# (number of nodes closer to j) +1 is actually the total nodes in subtree whose root is j. 
# from typing import List

from collections import deque
class Solution:
    def post_traverse(self, node, node2depth, list_node2neighbors, depth, answer, node2countNodesInSubtree):
        node2depth[node]=depth
        answer[0]+=depth
        if len(list_node2neighbors[node])==1 and depth!=0:
            #only has parent node
            node2countNodesInSubtree[node]=1
            return 1 #this subtree only has itself, return 1
        count=0
        for child in list_node2neighbors[node]:
            if node2depth[child]>=0:
                #this is visited parent
                continue
            count+=self.post_traverse(child,node2depth,list_node2neighbors,depth+1, answer, node2countNodesInSubtree)
        node2countNodesInSubtree[node]=count+1#plus current node itself
        return count+1


    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        

        answer=[0]*n
        node2depth=[-1]*n

        list_node2neighbors=[[] for i in range(n)]
        for i in range(len(edges)):
            list_node2neighbors[edges[i][0]].append(edges[i][1])
            list_node2neighbors[edges[i][1]].append(edges[i][0])

        depth=0


        nodes_in_same_depth=deque()

        #calculate answer[0]
        #count total number of nodes in subtree by setting each node as root of subtree
        node2countNodesInSubtree=[-1]*n
        self.post_traverse(0, node2depth, list_node2neighbors, depth, answer, node2countNodesInSubtree)

        #print(node2countNodesInSubtree)

        # # breath first search again to get answer[i]
        #breadth first search is a little faster than depth first search
        nodes_in_same_depth.clear()
        nodes_in_same_depth.append(0)
        depth=0
        while nodes_in_same_depth:
            length=len(nodes_in_same_depth)
            for j in range(length):
                node=nodes_in_same_depth.popleft()
                for node_child in list_node2neighbors[node]:
                    if node2depth[node_child]==depth+1:#child, not parent
                        nodes_in_same_depth.append(node_child)
                        answer[node_child]=answer[node]+(n-node2countNodesInSubtree[node_child])-node2countNodesInSubtree[node_child]
            depth+=1
        
        

        #print(answer)
        return answer
