# LC00738_Monotone_Increasing_Digits.py

# An integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.

# Given an integer n, return the largest number that is less than or equal to n with monotone increasing digits.

 

# Example 1:

# Input: n = 10
# Output: 9
# Example 2:

# Input: n = 1234
# Output: 1234
# Example 3:

# Input: n = 332
# Output: 299
 

# Constraints:

# 0 <= n <= 10**9

#12343215678
#12339999999

#765435889
#699999999

#7776521489
#6999999999

#1023
# 999

#1101
# 999

#Idea: find the left most digit that needs to reduce by 1, then, append 99999 after it.
#that digit'right neighbor is smaller(or same, then another right neighbor is smaller)
# if there is no such digit, then the original number is the answer. 

class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        if n<10:
            return n
        digits=[]
        num_temp=n
        while num_temp!=0:
            digits.append(num_temp%10)
            num_temp=num_temp//10
        digits.reverse()

        find_digit_index=-1
        for i in range(len(digits)):
            for j in range(i+1,len(digits)):
                if digits[i]>digits[j]:
                    find_digit_index=i
                    break
                elif digits[i]<digits[j]:
                    break
            if find_digit_index>=0:
                break

        if find_digit_index==-1:
            return n
        digits[find_digit_index]-=1
        for i in range(find_digit_index+1,len(digits)):
            digits[i]=9

        #convert digits back to num
        num=0
        for i in range(len(digits)):
            num=10*num+digits[i]
        return num
        
