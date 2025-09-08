# LC00788_Rotated_Digits.py

# An integer x is a good if after rotating each digit individually by 180 degrees, we get a valid number that is different from x. 
# Each digit must be rotated - we cannot choose to leave it alone.

# A number is valid if each digit remains a digit after rotation. For example:

# 0, 1, and 8 rotate to themselves,
# 2 and 5 rotate to each other (in this case they are rotated in a different direction, in other words, 2 or 5 gets mirrored),
# 6 and 9 rotate to each other, and
# the rest of the numbers do not rotate to any other number and become invalid.
# Given an integer n, return the number of good integers in the range [1, n].

 

# Example 1:

# Input: n = 10
# Output: 4
# Explanation: There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
# Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
# Example 2:

# Input: n = 1
# Output: 0
# Example 3:

# Input: n = 2
# Output: 1
 

# Constraints:

# 1 <= n <= 10*4


# Idea: there are 7 kind of digits (3+4) that are available. if we are free to manipulate 4 digits XXXX, then the total 
# candidates will be 7*7*7*7-3*3*3*3. For example, if n=5624, then
# total num =  0XXXX (7*7*7*7-3*3*3*3) + 1XXXX (7*7*7*7-3*3*3*3) + 2XXXX(2 is rotated, so 7*7*7*7) 
# + 50XXX (7*7*7-3*3*3) +51XXX(7*7*7-3*3*3) + 52XXX(7*7*7) + 55XXX(7*7*7)
# + 560X +561X
# + 5620+5621+5622

class Solution:
    def count_with_fixed_num_of_free_digits(self,digits,digit_index):
        Exist_2569=False
        for i in range(digit_index):
            if digits[i] in {3,4,7}:
                return 0
            elif digits[i] in {2,5,6,9}:
                Exist_2569=True

        num_of_free_digits=len(digits)-1-digit_index
        count_0or1or8_with_digits=7**num_of_free_digits-3**num_of_free_digits
        count_2or5or6or9_with_digits=7**num_of_free_digits
        count=0
        for i in range(digits[digit_index]+1):
            if i==digits[digit_index] and num_of_free_digits>0:
                break
            if i==0 or i==1 or i==8:
                if Exist_2569:
                    count+=count_2or5or6or9_with_digits
                else:
                    count+=count_0or1or8_with_digits
            elif i==2 or i==5 or i==6 or i==9:
                count+=count_2or5or6or9_with_digits
        
        return count

    def rotatedDigits(self, n: int) -> int:
        digits=[]
        temp_n=n
        while temp_n!=0:
            digits.append(temp_n%10)
            temp_n=temp_n//10
        digits.reverse()

        output=0
        for digit_index in range(len(digits)):
            output+=self.count_with_fixed_num_of_free_digits(digits,digit_index)
        return output
    
my_solu=Solution()
my_solu.rotatedDigits(857)
        
