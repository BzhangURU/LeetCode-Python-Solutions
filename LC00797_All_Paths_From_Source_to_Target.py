#LC00797_All_Paths_From_Source_to_Target


# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

# The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

 

# Example 1:


# Input: graph = [[1,2],[3],[3],[]]
# Output: [[0,1,3],[0,2,3]]
# Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
# Example 2:


# Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
# Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
 

# Constraints:

# n == graph.length
# 2 <= n <= 15
# 0 <= graph[i][j] < n
# graph[i][j] != i (i.e., there will be no self-loops).
# All the elements of graph[i] are unique.
# The input graph is guaranteed to be a DAG.

#Idea: use depth first search. 

#Python 3:

def traverse_graph(dict_node_edges, cur_node, results, cur_path, goal):
    cur_path.append(cur_node)
    #print(cur_path)
    if cur_node==goal:
        one_result=cur_path.copy()
        results.append(one_result)

    for next_node in dict_node_edges[cur_node]:
        traverse_graph(dict_node_edges,next_node,results,cur_path, goal)


    cur_path.pop()

class Solution(object):
#class Solution():
    #def allPathsSourceTarget(self, graph):
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """

        #save each node's descendants
        dict_node_edges={}
        for i in range(len(graph)):
            dict_node_edges[i]=set()
            #print('Currently visiting {}'.format(i))
            for j in range(len(graph[i])):
                dict_node_edges[i].add(graph[i][j])
                #print('     node {} added'.format(graph[i][j]))


        results=[]
        cur_path=[]
        traverse_graph(dict_node_edges,0,results,cur_path,len(graph)-1)

        return results

graph = [[1,2],[3],[3],[]]
my_class=Solution()
print(my_class.allPathsSourceTarget(graph))
