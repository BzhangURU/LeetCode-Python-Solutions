#This solution takes runtime of 0 ms, which beats 100.00% other submissions at the time of submission.

# LC00785_Is_Graph_Bipartite
# There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. 
# You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent 
# to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. 
# The graph has the following properties:

# There are no self-edges (graph[u] does not contain u).
# There are no parallel edges (graph[u] does not contain duplicate values).
# If v is in graph[u], then u is in graph[v] (the graph is undirected).
# The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
# A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge 
# in the graph connects a node in set A and a node in set B.

# Return true if and only if it is bipartite.

 

# Example 1:


# Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
# Output: false
# Explanation: There is no way to partition the nodes into two independent sets such that every edge connects 
# a node in one and a node in the other.
# Example 2:


# Input: graph = [[1,3],[0,2],[1,3],[0,2]]
# Output: true
# Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.
 

# Constraints:

# graph.length == n
# 1 <= n <= 100
# 0 <= graph[u].length < n
# 0 <= graph[u][i] <= n - 1
# graph[u] does not contain u.
# All the values of graph[u] are unique.
# If graph[u] contains v, then graph[v] contains u.

#Idea: 
#breadth first search
#if a node is new, then we set its label to opposite of its source
#if a node was visited, then we check if the label is correct

from collections import deque

#class Solution(object):
class Solution():
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n=len(graph)
        dict_node_group_label={}
        adj_nodes=deque()
        
        #print_layer=0
        
        #if node was or is in adj_nodes, then it is visited!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        unvisited_nodes=set()
        for i in range(n):
            unvisited_nodes.add(i)
        #There is chance that a node is not connected to any other nodes, so that node is not in adj_nodes ever. 
        
        
        while len(unvisited_nodes)>0:
            #start a new connected graph
            #start_node=0
            start_node=unvisited_nodes.pop()
            adj_nodes.append(start_node)
            target_label_in_this_round=1
            
            while len(adj_nodes)>0:
                target_label_in_this_round=1-target_label_in_this_round
                #print_layer+=1
                #print('\nLayer {}, elements in adj_nodes:'.format(print_layer))
                #print(adj_nodes)
                
                #if print_layer>5:
                #    return False
                
                for i in range(len(adj_nodes)):
                    cur_node=adj_nodes.popleft()
                    #print('Visiting node {}'.format(cur_node))
                    if cur_node not in dict_node_group_label:
                        dict_node_group_label[cur_node]=target_label_in_this_round
                        #print('group label set to {}'.format(target_label_in_this_round))
                    elif dict_node_group_label[cur_node]!=target_label_in_this_round:
                        #print('group label is not {}, return False'.format(target_label_in_this_round))
                        return False
                    if cur_node in unvisited_nodes:
                        unvisited_nodes.remove(cur_node)
                    for j in range(len(graph[cur_node])):
                        if graph[cur_node][j] in unvisited_nodes:
                            adj_nodes.append(graph[cur_node][j])
                            unvisited_nodes.remove(graph[cur_node][j])
                            #print('    Adding {} into adj_nodes'.format(graph[cur_node][j]))
                        
                        if graph[cur_node][j] not in dict_node_group_label:
                            dict_node_group_label[graph[cur_node][j]]=1-target_label_in_this_round
                            #print('    group label of {} set to {}'.format(graph[cur_node][j], 1-target_label_in_this_round))
                        elif dict_node_group_label[graph[cur_node][j]]!=1-target_label_in_this_round:
                                #print('    group label of {} is not {}, return False'.format(graph[cur_node][j],target_label_in_this_round))
                                return False
                    
                            
                
                                
        return True
