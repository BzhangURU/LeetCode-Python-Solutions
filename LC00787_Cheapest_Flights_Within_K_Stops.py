#LC00787_Cheapest_Flights_Within_K_Stops


# There are n cities connected by some number of flights. You are given an array flights 
# where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi 
# to city toi with cost pricei.

# You are also given three integers src, dst, and k, return the cheapest price from src to dst 
# with at most k stops. If there is no such route, return -1.

 

# Example 1:


# Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
# Output: 700
# Explanation:
# The graph is shown above.
# The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
# Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
# Example 2:


# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
# Output: 200
# Explanation:
# The graph is shown above.
# The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.
# Example 3:


# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
# Output: 500
# Explanation:
# The graph is shown above.
# The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.
 

# Constraints:

# 1 <= n <= 100
# 0 <= flights.length <= (n * (n - 1) / 2)
# flights[i].length == 3
# 0 <= fromi, toi < n
# fromi != toi
# 1 <= pricei <= 104
# There will not be any multiple flights between two cities.
# 0 <= src, dst, k < n
# src != dst

from collections import deque

#class Solution(object):
class Solution():
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        dict_adj_nodes={}
        for edge in flights:
            if edge[0] not in dict_adj_nodes:
                dict_adj_nodes[edge[0]]={edge[1]:edge[2]}
            else:
                dict_adj_nodes[edge[0]][edge[1]]=edge[2]
                
        node_prices=[-1]*n
        node_prices[src]=0
    
        adj_nodes_queue=deque()
        adj_nodes_queue.append(src)
        
        count_stop=-1
        #breath first search
        while adj_nodes_queue:
            if count_stop>=k:
                break
            
            count_stop+=1
            #print('count_stop={}'.format(count_stop))
            count_adj_nodes=len(adj_nodes_queue)
            temp_dict_update_price={}
            for i in range(count_adj_nodes):
                cur_node=adj_nodes_queue.popleft()
                #update price in the end of each round
                
                if cur_node in dict_adj_nodes:
                    for next_node in dict_adj_nodes[cur_node]:
                        if node_prices[next_node]<0 or node_prices[next_node]>node_prices[cur_node]+dict_adj_nodes[cur_node][next_node]:
                            #We can not update immediately, as we may reach a node that takes higher price but shorter stop. 
                            #node_prices[next_node]=node_prices[cur_node]+dict_adj_nodes[cur_node][next_node]
                            if next_node not in temp_dict_update_price:
                                temp_dict_update_price[next_node]=node_prices[cur_node]+dict_adj_nodes[cur_node][next_node]
                                #print('    record {}: price {}'.format(next_node,temp_dict_update_price[next_node]))
                            elif temp_dict_update_price[next_node]>node_prices[cur_node]+dict_adj_nodes[cur_node][next_node]:
                                temp_dict_update_price[next_node]=node_prices[cur_node]+dict_adj_nodes[cur_node][next_node]
                                #print('    record {}: price {}'.format(next_node,temp_dict_update_price[next_node]))
                            adj_nodes_queue.append(next_node)
                            
            for node in temp_dict_update_price:
                node_prices[node]=temp_dict_update_price[node]
                #print('    update {}: price {}'.format(node,temp_dict_update_price[node]))
                        
        return node_prices[dst]
        
        
flights=[[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
class_s=Solution()
print (class_s.findCheapestPrice(4, flights, 0, 3, 1))
