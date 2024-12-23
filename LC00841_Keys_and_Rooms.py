# LC00841_Keys_and_Rooms.py

# There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. 
# Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

# When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, 
# denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

# Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, 
# return true if you can visit all the rooms, or false otherwise.

 

# Example 1:

# Input: rooms = [[1],[2],[3],[]]
# Output: true
# Explanation: 
# We visit room 0 and pick up key 1.
# We then visit room 1 and pick up key 2.
# We then visit room 2 and pick up key 3.
# We then visit room 3.
# Since we were able to visit every room, we return true.
# Example 2:

# Input: rooms = [[1,3],[3,0,1],[2],[0]]
# Output: false
# Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.
 

# Constraints:

# n == rooms.length
# 2 <= n <= 1000
# 0 <= rooms[i].length <= 1000
# 1 <= sum(rooms[i].length) <= 3000
# 0 <= rooms[i][j] < n
# All the values of rooms[i] are unique.
from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        set_explored_rooms=set()
        set_rooms_to_explore=set()
        set_rooms_to_explore.add(0)

        while set_rooms_to_explore:
            room_ind=set_rooms_to_explore.pop()
            for key_ind in rooms[room_ind]:
                if key_ind not in set_explored_rooms and \
                    key_ind not in set_rooms_to_explore and key_ind!=room_ind:
                    set_rooms_to_explore.add(key_ind)
            set_explored_rooms.add(room_ind)
        if len(set_explored_rooms)<len(rooms):
            return False
        else:
            return True
        
my_solu=Solution()
rooms=[[1,3],[3,0,1],[2],[0]]

print(my_solu.canVisitAllRooms(rooms))
