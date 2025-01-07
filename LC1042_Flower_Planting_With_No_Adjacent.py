# LC1042_Flower_Planting_With_No_Adjacent.py

# You have n gardens, labeled from 1 to n, and an array paths where paths[i] = [xi, yi] 
# describes a bidirectional path between garden xi to garden yi. In each garden, you want 
# to plant one of 4 types of flowers.

# All gardens have at most 3 paths coming into or leaving it.

# Your task is to choose a flower type for each garden such that, for any two gardens 
# connected by a path, they have different types of flowers.

# Return any such a choice as an array answer, where answer[i] is the type of flower 
# planted in the (i+1)th garden. The flower types are denoted 1, 2, 3, or 4. It is guaranteed an answer exists.

 

# Example 1:

# Input: n = 3, paths = [[1,2],[2,3],[3,1]]
# Output: [1,2,3]
# Explanation:
# Gardens 1 and 2 have different types.
# Gardens 2 and 3 have different types.
# Gardens 3 and 1 have different types.
# Hence, [1,2,3] is a valid answer. Other valid answers include [1,2,4], [1,4,2], and [3,2,1].
# Example 2:

# Input: n = 4, paths = [[1,2],[3,4]]
# Output: [1,2,1,2]
# Example 3:

# Input: n = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
# Output: [1,2,3,4]
 

# Constraints:

# 1 <= n <= 10**4
# 0 <= paths.length <= 2 * 10**4
# paths[i].length == 2
# 1 <= xi, yi <= n
# xi != yi
# Every garden has at most 3 paths coming into or leaving it.

#Idea: add color one by one, since All gardens have at most 3 paths coming into or leaving it, 
# we can always find an available color for each one. 
from typing import List
class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        each_garden_color=[0]*(n+1)

        dict_adj_nodes={}
        for path in paths:
            if path[0] not in dict_adj_nodes:
                dict_adj_nodes[path[0]]=set()
            dict_adj_nodes[path[0]].add(path[1])

            if path[1] not in dict_adj_nodes:
                dict_adj_nodes[path[1]]=set()
            dict_adj_nodes[path[1]].add(path[0])

        for i in range(1,n+1):
            unused_colors=set([1,2,3,4])
            if i not in dict_adj_nodes:
                each_garden_color[i]=1
            else:
                for adj_node in dict_adj_nodes[i]:
                    if each_garden_color[adj_node]>0 and each_garden_color[adj_node] in unused_colors:
                        unused_colors.remove(each_garden_color[adj_node])
                each_garden_color[i]=unused_colors.pop()

        del each_garden_color[0]
        return each_garden_color
        

