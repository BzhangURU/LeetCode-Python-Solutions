# LC00735_Asteroid_Collision.py

# We are given an array asteroids of integers representing asteroids in a row. The indices of the asteriod 
# in the array represent their relative position in space.

# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive 
#                         meaning right, negative meaning left). Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. 
# If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

# Example 1:

# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
# Example 2:

# Input: asteroids = [8,-8]
# Output: []
# Explanation: The 8 and -8 collide exploding each other.
# Example 3:

# Input: asteroids = [10,2,-5]
# Output: [10]
# Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
 

# Constraints:

# 2 <= asteroids.length <= 104
# -1000 <= asteroids[i] <= 1000
# asteroids[i] != 0

from collections import deque

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        output=[]
        my_q=deque()
        for i in range(len(asteroids)):
            if asteroids[i]>0:
                my_q.append(asteroids[i])
            else:
                if len(my_q)==0:
                    output.append(asteroids[i])
                else:
                    find_equal=False
                    while len(my_q)>0 and my_q[-1]<=abs(asteroids[i]):
                        if my_q[-1]==abs(asteroids[i]):
                            find_equal=True
                            my_q.pop()
                            break
                        my_q.pop()
                    if len(my_q)==0 and find_equal==False:
                        output.append(asteroids[i])
        while len(my_q)>0:
            output.append(my_q.popleft())
        return output
        

