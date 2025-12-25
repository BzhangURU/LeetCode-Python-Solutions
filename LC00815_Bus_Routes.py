# LC00815_Bus_Routes.py

# You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

# For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the 
# sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
# You will start at the bus stop source (You are not on any bus initially), 
# and you want to go to the bus stop target. You can travel between bus stops by buses only.

# Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

 

# Example 1:

# Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
# Output: 2
# Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
# Example 2:

# Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
# Output: -1
 

 

# Constraints:

# 1 <= routes.length <= 500.
# 1 <= routes[i].length <= 10**5
# All the values of routes[i] are unique.
# sum(routes[i].length) <= 10**5
# 0 <= routes[i][j] < 10**6
# 0 <= source, target < 10**6

from typing import List

from collections import deque
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        stops_mapping_to_route_indexes={}
        visited_route_indexes=set()
        stops_mapping_to_least_number_buses_to_reach={}

        #initialize stop_mapping_to_route_indexes
        for route_ind in range(len(routes)):
            for stop in routes[route_ind]:
                if stop not in stops_mapping_to_route_indexes:
                    stops_mapping_to_route_indexes[stop]=set()
                stops_mapping_to_route_indexes[stop].add(route_ind)

        if source == target:
            return 0
        if source not in stops_mapping_to_route_indexes or target not in stops_mapping_to_route_indexes:
            return -1

        stops_to_visit=deque()
        stops_to_visit.append(source)
        stops_mapping_to_least_number_buses_to_reach[source]=0

        least_number_buses=0

        while len(stops_to_visit)>0:
            least_number_buses+=1
            queue_length=len(stops_to_visit)
            for i in range(queue_length):
                cur_stop=stops_to_visit.popleft()
                route_indexes=stops_mapping_to_route_indexes[cur_stop]
                #explore more stops based on route_indexes
                for route_ind in route_indexes:
                    if route_ind in visited_route_indexes:
                        continue
                    visited_route_indexes.add(route_ind)
                    for stop in routes[route_ind]:
                        if stop not in stops_mapping_to_least_number_buses_to_reach:
                            stops_mapping_to_least_number_buses_to_reach[stop]=least_number_buses
                            stops_to_visit.append(stop)

        if target not in stops_mapping_to_least_number_buses_to_reach:
            return -1
        else:
            return stops_mapping_to_least_number_buses_to_reach[target]


my_solu=Solution()
routes=[[1,2,7],[3,6,7]]
source=8
target=6

# routes=[[1,2,7],[3,6,7]]
# source=1
# target=6

print(my_solu.numBusesToDestination(routes,source,target))



        

