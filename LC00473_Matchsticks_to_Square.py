# LC00473_Matchsticks_to_Square.py

# You are given an integer array matchsticks where matchsticks[i] is 
# the length of the ith matchstick. You want to use all the matchsticks 
# to make one square. You should not break any stick, but you can link them up, 
# and each matchstick must be used exactly one time.

# Return true if you can make this square and false otherwise.

 

# Example 1:


# Input: matchsticks = [1,1,2,2,2]
# Output: true
# Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
# Example 2:

# Input: matchsticks = [3,3,3,3,4]
# Output: false
# Explanation: You cannot find a way to form a square with all the matchsticks.
 

# Constraints:

# 1 <= matchsticks.length <= 15
# 1 <= matchsticks[i] <= 10**8

# Idea: try all the options
from typing import List
class Solution:
    def DP(self,matchsticks,goal,cur_lengths,cur_index):
        if cur_index==len(matchsticks):
            found_ans=True
            for i in range(4):
                if cur_lengths[i]!=goal:
                    found_ans=False
            return found_ans
        
        set_visited_length=set()
        for i in range(4):
            if cur_lengths[i] not in set_visited_length and cur_lengths[i]+matchsticks[cur_index]<=goal:
                cur_lengths[i]+=matchsticks[cur_index]
                result=self.DP(matchsticks,goal,cur_lengths,cur_index+1)
                if result:
                    return True
                cur_lengths[i]-=matchsticks[cur_index]
                set_visited_length.add(cur_lengths[i])
        return False

    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks)<4:
            return False
        all_sum=sum(matchsticks)
        goal=all_sum//4
        if all_sum%4!=0:
            return False
        matchsticks.sort(reverse=True)
        cur_lengths=[0]*4
        print('debug place 001')
        return self.DP(matchsticks,goal,cur_lengths,0)
    
my_solu=Solution()
matchsticks=[5,5,5,5,4,4,4,4,3,3,3,3]
print(my_solu.makesquare(matchsticks))

        
