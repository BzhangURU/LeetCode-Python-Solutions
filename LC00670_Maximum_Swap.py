# LC00670_Maximum_Swap.py

# You are given an integer num. You can swap two digits at most once to get the maximum valued number.

# Return the maximum valued number you can get.

 

# Example 1:

# Input: num = 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
# Example 2:

# Input: num = 9973
# Output: 9973
# Explanation: No swap.
 

# Constraints:

# 0 <= num <= 10**8

# Idea: search from left digits, immediately change the digit that is not the max compare to all its right.


class Solution:
    def maximumSwap(self, num: int) -> int:
        if num<10:
            return num
        digits=[]
        num2=num
        while num2!=0:
            digits.append(num2%10)
            num2=num2//10
        digits.reverse()

        max_digit_so_far=digits[-1]
        max_digit_position=len(digits)-1

        cur_ans_left=-1
        cur_ans_right=-1

        for pos in range(len(digits)-2,-1,-1):
            if digits[pos]<max_digit_so_far:
                cur_ans_left=pos
                cur_ans_right=max_digit_position
            if digits[pos]>max_digit_so_far:
                max_digit_so_far=digits[pos]
                max_digit_position=pos

        if cur_ans_left>=0:
            digit=digits[cur_ans_left]
            digits[cur_ans_left]=digits[cur_ans_right]
            digits[cur_ans_right]=digit
            result=0
            for i in range(len(digits)):
                result=result*10+digits[i]
            return result
        else:
            return num



        
