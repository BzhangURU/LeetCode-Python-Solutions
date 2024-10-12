# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, 
# and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are 
# directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.

# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2

# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
 

# Constraints:

# 1 <= n <= 200
# n == isConnected.length
# n == isConnected[i].length
# isConnected[i][j] is 1 or 0.
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]

class Solution(object):
  # My idea: use dynamic programming, if the current vertice is connected to multiple vertices,
  # then make those vertices connected, and remove current vertice. 
    def find_num_provinces(self, isConnected, n):
        if n==1:
            return 1
        count_ind_n_minus1_connected_vertices=0
        list_connected_vertices=[]
        for i in range(0,n-1):
            if isConnected[i][n-1]==1:
                count_ind_n_minus1_connected_vertices+=1
                list_connected_vertices.append(i)
        if count_ind_n_minus1_connected_vertices==0:
            return 1+self.find_num_provinces(isConnected, n-1)
        elif count_ind_n_minus1_connected_vertices==1:
            return self.find_num_provinces(isConnected, n-1)
        else:
            for i in range(count_ind_n_minus1_connected_vertices-1):
                for j in range(i+1,count_ind_n_minus1_connected_vertices):
                    isConnected[list_connected_vertices[i]][list_connected_vertices[j]]=1
                    isConnected[list_connected_vertices[j]][list_connected_vertices[i]]=1
            return self.find_num_provinces(isConnected, n-1)

    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n=len(isConnected)
        
        return self.find_num_provinces(isConnected, n)
