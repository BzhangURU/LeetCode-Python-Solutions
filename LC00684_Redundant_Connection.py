# LC00684_Redundant_Connection
# In this problem, a tree is an undirected graph that is connected and has no cycles.

# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one 
# additional edge added. The added edge has two different vertices chosen from 1 to n, and 
# was not an edge that already existed. The graph is represented as an array edges of length n 
# where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If 
# there are multiple answers, return the answer that occurs last in the input.

# Example 1:
# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]

# Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
# Output: [1,4]

# Constraints:

# n == edges.length
# 3 <= n <= 1000
# edges[i].length == 2
# 1 <= ai < bi <= edges.length
# ai != bi
# There are no repeated edges.
# The given graph is connected.

#idea: first use hash map to store each node's directly connected nodes to build graph,
# then use graph dsf traversal to find all node in the circle. (In the meantime record the path)
# then loop through the edges to find the last edge in the circle
from collections import deque

class Solution(object):
    
    def traverse_graph_to_find_circle(self, dict_neighbor_nodes, prev_node, cur_node, visited_nodes, path_q, set_of_nodes_in_circle):
        if visited_nodes[cur_node]==1:
            #find circle
            circle_start=False
            for node in path_q:
                if node==cur_node:
                    circle_start=True
                if circle_start:
                    set_of_nodes_in_circle.add(node)
            return 
        
        path_q.append(cur_node)
        visited_nodes[cur_node]=1
        
        for node in dict_neighbor_nodes[cur_node]:
            if node!=prev_node:
                self.traverse_graph_to_find_circle(dict_neighbor_nodes, cur_node, node, visited_nodes, path_q, set_of_nodes_in_circle)
                if len(set_of_nodes_in_circle)>0:
                    break
                
        path_q.pop()
        
        return 
    # idea: the last redundant edge should introduce no new node.
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        #step 1: build graph
        n=len(edges)
        dict_neighbor_nodes={}
        
        for i in range(len(edges)):
            if edges[i][0] not in dict_neighbor_nodes:
                dict_neighbor_nodes[edges[i][0]]={edges[i][1]}#value is a set
            else:
                dict_neighbor_nodes[edges[i][0]].add(edges[i][1])
                
            if edges[i][1] not in dict_neighbor_nodes:
                dict_neighbor_nodes[edges[i][1]]={edges[i][0]}#value is a set
            else:
                dict_neighbor_nodes[edges[i][1]].add(edges[i][0])
                
        #step 2: find the only circle in graph
        
        path_q=deque()
        visited_nodes=[0]*(n+1)# first node is 1, last node is n
        set_of_nodes_in_circle=set()
        start_node=1
        self.traverse_graph_to_find_circle(dict_neighbor_nodes, -1, start_node, visited_nodes, path_q, set_of_nodes_in_circle)
        
        # step 3: find the last edge in circle
        output_edge=[0,0]
        for edge in edges:
            if edge[0] in set_of_nodes_in_circle and edge[1] in set_of_nodes_in_circle:
                output_edge=edge
        
        return output_edge
