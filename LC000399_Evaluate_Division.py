#LC000399_Evaluate_Division

# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] 
# and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer 
# for Cj / Dj = ?.

# Return the answers to all queries. If a single answer cannot be determined, return -1.0.

# Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and 
# that there is no contradiction.

# Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

 

# Example 1:

# Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
# Explanation: 
# Given: a / b = 2.0, b / c = 3.0
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
# return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
# note: x is undefined => -1.0
# Example 2:

# Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# Output: [3.75000,0.40000,5.00000,0.20000]
# Example 3:

# Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
# Output: [0.50000,2.00000,-1.00000,-1.00000]
 

# Constraints:

# 1 <= equations.length <= 20
# equations[i].length == 2
# 1 <= Ai.length, Bi.length <= 5
# values.length == equations.length
# 0.0 < values[i] <= 20.0
# 1 <= queries.length <= 20
# queries[i].length == 2
# 1 <= Cj.length, Dj.length <= 5
# Ai, Bi, Cj, Dj consist of lower case English letters and digits.
from collections import deque
class vertice():
    def __init__(self,name):
        self.name=name
        self.edges={}
    def build_edge(self, adj_vertice_name,weight):
        self.edges[adj_vertice_name]=weight

class Solution(object):
    
    #The function returns answer for one query
    def check_one_division(self,dict_name_str_to_vertice,query):
        name_str0=query[0]
        name_str1=query[1]
        if name_str0 not in dict_name_str_to_vertice:
            return -1.0
        if name_str0==name_str1:
            return 1.0
        
        deque_name=deque()
        vertice=dict_name_str_to_vertice[name_str0]
        deque_name.append(vertice.name)
        
        #also store the division results
        name_str_visited={name_str0:1.0}
        
        
        while(deque_name):
            cur_name=deque_name.popleft()
            cur_v=dict_name_str_to_vertice[cur_name]
            
            for adj_vertice_name in cur_v.edges:
                if adj_vertice_name not in name_str_visited:
                    name_str_visited[adj_vertice_name]=name_str_visited[cur_name]*cur_v.edges[adj_vertice_name]
                    if adj_vertice_name==name_str1:
                        return name_str_visited[adj_vertice_name]
                    deque_name.append(adj_vertice_name)
                    
        return -1.0
                    
    
    
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        
        dict_name_str_to_vertice={}
        
        #first build graph
        for i in range(len(equations)):
            #if not seen before, create new vertice
            if equations[i][0] not in dict_name_str_to_vertice:
                vertice0=vertice(equations[i][0])
                dict_name_str_to_vertice[equations[i][0]]=vertice0
            else:
                vertice0=dict_name_str_to_vertice[equations[i][0]]
                
            if equations[i][1] not in dict_name_str_to_vertice:
                vertice1=vertice(equations[i][1])
                dict_name_str_to_vertice[equations[i][1]]=vertice1
            else:
                vertice1=dict_name_str_to_vertice[equations[i][1]]
                
            #build edges
                
            vertice0.build_edge(equations[i][1], values[i])
            vertice1.build_edge(equations[i][0], 1.0/values[i])
            
        output=[-1.0]*len(queries)
        for i in range(len(queries)):
            output[i]=self.check_one_division(dict_name_str_to_vertice, queries[i])
            
        return output
