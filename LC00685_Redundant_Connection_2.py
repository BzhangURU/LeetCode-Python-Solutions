# This solution beats 100.00% of other submissions with runtime of 4 ms in Python. 



# In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) for which 
# all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node 
# which has no parents.

# The given input is a directed graph that started as a rooted tree with n nodes (with distinct values from 1 to n), 
# with one additional directed edge added. The added edge has two different vertices chosen from 1 to n, and was not 
# an edge that already existed.

# The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [ui, vi] that represents a 
# directed edge connecting nodes ui and vi, where ui is a parent of child vi.

# Return an edge that can be removed so that the resulting graph is a rooted tree of n nodes. If there are multiple 
# answers, return the answer that occurs last in the given 2D-array.

 

# Example 1:


# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]
# Example 2:


# Input: edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]
# Output: [4,1]
 

# Constraints:

# n == edges.length
# 3 <= n <= 1000
# edges[i].length == 2
# 1 <= ui, vi <= n
# ui != vi

#idea: first use hash map to store each node's directly connected nodes to build graph,
# then use graph dsf traversal to find all node in the circle. (In the meantime record the path)
# then loop through the edges to find the last edge in the circle

#There is at most one node that have two parents. 
#In the circle, there are two types. 
#First, A is root, there are two paths from A to the final destination B. 
#In this case, delete last edge that has node B. 


#Second, it is a clockwise circle. (one path from A to B, but has edge B-->A)
#In this case, there is at most ONE node outside circle that points to a node in the circle. If that is the case (ONE node),
#delete the edge in the circle that points to the circle node that has two parents. Otherwise it's OK to delete any edge in circle. 


from collections import deque

class Solution(object):
#class Solution():
    
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
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        #step 1: build graph and search for root node
        n=len(edges)
        dict_neighbor_nodes={}
        
        #record number of parents for each node
        num_par=[0]*(n+1)
        
        
        #find_duplicated_but_reversed_direction_edge
        duplicated_edges=[-1,-1]
        
        for i in range(len(edges)):
            if edges[i][0] not in dict_neighbor_nodes:
                dict_neighbor_nodes[edges[i][0]]={edges[i][1]}#value is a set
            else:
                if edges[i][1] in dict_neighbor_nodes[edges[i][0]]:
                    duplicated_edges=[edges[i][0],edges[i][1]]
                dict_neighbor_nodes[edges[i][0]].add(edges[i][1])
                
            if edges[i][1] not in dict_neighbor_nodes:
                dict_neighbor_nodes[edges[i][1]]={edges[i][0]}#value is a set
            else:
                dict_neighbor_nodes[edges[i][1]].add(edges[i][0])
            num_par[edges[i][1]]+=1
                
        #step 2: find the only circle in graph
        
        if duplicated_edges[0]!=-1:
            set_of_nodes_in_circle={duplicated_edges[0],duplicated_edges[1]}
        else:
            path_q=deque()
            visited_nodes=[0]*(n+1)# first node is 1, last node is n
            set_of_nodes_in_circle=set()
            start_node=1
            self.traverse_graph_to_find_circle(dict_neighbor_nodes, -1, start_node, visited_nodes, path_q, set_of_nodes_in_circle)
        
        # print("set of nodes in circle")
        # for i in set_of_nodes_in_circle:
        #     print(i)
        
        # step 3: find the last edge in circle
        
        # print("num of parents for each node")
        # for i in range(1,n+1):
        #     print('{}: {}'.format(i,num_par[i]))
        
        output_edge=[0,0]
        #there is at most one node with 2 parents
        node_with_2_parents_found=False
        for edge in edges:
            if edge[0] in set_of_nodes_in_circle and edge[1] in set_of_nodes_in_circle:
                if node_with_2_parents_found==False or num_par[edge[1]]>1:
                    output_edge=edge
                if num_par[edge[1]]>1:
                    node_with_2_parents_found=True
                    
        #print(output_edge)
        
        return output_edge
