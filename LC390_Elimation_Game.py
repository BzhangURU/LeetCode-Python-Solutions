# LC390_Elimation_Game.py

# You have a list arr of all integers in the range [1, n] sorted in a strictly 
# increasing order. Apply the following algorithm on arr:

# Starting from left to right, remove the first number and every other number 
# afterward until you reach the end of the list.
# Repeat the previous step again, but this time from right to left, remove the 
# rightmost number and every other number from the remaining numbers.
# Keep repeating the steps again, alternating left to right and right to left, 
# until a single number remains.
# Given the integer n, return the last number that remains in arr.

 

# Example 1:

# Input: n = 9
# Output: 6
# Explanation:
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# arr = [2, 4, 6, 8]
# arr = [2, 6]
# arr = [6]
# Example 2:

# Input: n = 1
# Output: 1
 

# Constraints:

# 1 <= n <= 10**9

# challenging topic I finally solved by myself.
# My idea: for example, if it is 9, we get 9  from left->  4  from right->  2  from left->  1,
# then we reverse the process, 1->2 by "from left": the index of the final remaining number is from 0 to 1.

class Solution:
    #return last remaining index!!!!!! (It is index!!!)
    def my_last_remaining(self, cur_total_before_operation, operation_is_from_left):
        if cur_total_before_operation==1:
            return 0
        elif operation_is_from_left==1:
            result_ind=self.my_last_remaining(cur_total_before_operation//2,1-operation_is_from_left)
            return result_ind*2+1
        else:
            result_ind=self.my_last_remaining(cur_total_before_operation//2,1-operation_is_from_left)
            if cur_total_before_operation%2==0:
                return result_ind*2
            else:
                return result_ind*2+1

    def lastRemaining(self, n: int) -> int:
        return 1+self.my_last_remaining(n,1)
        
        

