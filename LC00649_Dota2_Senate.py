# LC00649_Dota2_Senate.py

# In the world of Dota2, there are two parties: the Radiant and the Dire.

# The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. 
# The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:

# Ban one senator's right: A senator can make another senator lose all his rights in this and all the following rounds.
# Announce the victory: If this senator found the senators who still have rights to vote are all from the same party, 
# he can announce the victory and decide on the change in the game.
# Given a string senate representing each senator's party belonging. The character 'R' and 'D' represent the Radiant 
# party and the Dire party. Then if there are n senators, the size of the given string will be n.

# The round-based procedure starts from the first senator to the last senator in the given order. This procedure will 
# last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.

# Suppose every senator is smart enough and will play the best strategy for his own party. Predict which party will 
# finally announce the victory and change the Dota2 game. The output should be "Radiant" or "Dire".

 

# Example 1:

# Input: senate = "RD"
# Output: "Radiant"
# Explanation: 
# The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
# And the second senator can't exercise any rights anymore since his right has been banned. 
# And in round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.
# Example 2:

# Input: senate = "RDD"
# Output: "Dire"
# Explanation: 
# The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
# And the second senator can't exercise any rights anymore since his right has been banned. 
# And the third senator comes from Dire and he can ban the first senator's right in round 1. 
# And in round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.
 

# Constraints:

# n == senate.length
# 1 <= n <= 10**4
# senate[i] is either 'R' or 'D'.

# Idea: define a R_advantage to know which senate losses vote, then shrink the string and run second round. 

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        count_R=0
        count_D=0
        for i in range(len(senate)):
            if senate[i]=='R':
                count_R+=1
            else:
                count_D+=1
        if count_R==0:
            return "Dire"
        elif count_D==0:
            return "Radiant"

        senate_can_vote=[True]*len(senate)

        R_advantage=0
        for i in range(len(senate)):
            if senate[i]=='R':
                if R_advantage<0:
                    senate_can_vote[i]=False
                R_advantage+=1
            else:
                #'D'
                if R_advantage>0:
                    senate_can_vote[i]=False
                R_advantage-=1
        list_senate=[]  
        for i in range(len(senate)):
            if senate_can_vote[i]:
                if R_advantage>0:
                    if senate[i]=='D':
                        R_advantage-=1
                    else:
                        list_senate.append(senate[i])
                elif R_advantage<0:
                    if senate[i]=='R':
                        R_advantage+=1
                    else:
                        list_senate.append(senate[i])
                else:
                    list_senate.append(senate[i])
        senate=''.join(list_senate)
        print(senate)
        return self.predictPartyVictory(senate)

my_solu=Solution()
my_solu.predictPartyVictory("RDD")    

                    



