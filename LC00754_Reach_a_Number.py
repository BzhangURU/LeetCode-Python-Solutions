# LC00754_Reach_a_Number.py

# You are standing at position 0 on an infinite number line. There is a destination at position target.

# You can make some number of moves numMoves so that:

# On each move, you can either go left or right.
# During the ith move (starting from i == 1 to i == numMoves), you take i steps in the chosen direction.
# Given the integer target, return the minimum number of moves required (i.e., the minimum numMoves) 
# to reach the destination.

 

# Example 1:

# Input: target = 2
# Output: 3
# Explanation:
# On the 1st move, we step from 0 to 1 (1 step).
# On the 2nd move, we step from 1 to -1 (2 steps).
# On the 3rd move, we step from -1 to 2 (3 steps).
# Example 2:

# Input: target = 3
# Output: 2
# Explanation:
# On the 1st move, we step from 0 to 1 (1 step).
# On the 2nd move, we step from 1 to 3 (2 steps).
 

# Constraints:

# -10**9 <= target <= 10**9
# target != 0

# Idea: always try to go right, see how many steps to reach, then check redundant steps
# For example, a target is 1+2+3+...+99+8, then redundant steps is 100-8=92(even), only on 46th step, turn left,

# if a target is 1+2+3+...+99+1:  1+2+3+...+99 (-100+101)
# if a target is 1+2+3+...+99+99:   1+2+3+...+99+100+101(only minus 52)           Not:          1+2+3+...+99 (+100+101-102)
# if a target is 1+2+3+...+99+98: redundant is 100-98==2(even number), -1+2+3+...+99 +100
# if a target is 1+2+3+...+99+2: redundant is 100-2==98(even number), 1+2+3+...+99 +100 (only 49 is minus)

# if a target is 1+2+3+...+100+1: redundant is 101-1==100(even number), 1+2+3+...+100+101 (only minus 50)
# if a target is 1+2+3+...+100+99: redundant is 101-99==2(even number),  1+2+3+...+100+101(only minus 1)           
# if a target is 1+2+3+...+100+100: 1+2+3+...+100+101+102-103
# if a target is 1+2+3+...+100+2: 1+2+3+...+100+101+102-103 (only 49 is minus)

#(1+n)*n/2=

class Solution:
    def reachNumber(self, target: int) -> int:
        target=abs(target)

        #first get steps_beyond_target

        left_bound=1
        right_bound=5*(10**4)
        #find left_bound's max steps <= target < right_bound's max steps

        while left_bound+1<right_bound:
            middle=(left_bound+right_bound)//2
            if middle*(middle+1)//2<=target:
                left_bound=middle
            else:
                right_bound=middle
        print('left: {}, right: {}'.format(left_bound,right_bound))

        left_bound_steps=left_bound*(left_bound+1)//2
        if left_bound_steps==target:
            return left_bound
        elif (left_bound_steps+left_bound+1-target)%2==0:#even number
            return left_bound+1
        elif left_bound%2==1:
            return left_bound+2
        else:
            return left_bound+3

my_solu=Solution()
print(my_solu.reachNumber(9))


