# LC00633_Sum_of_Square_Numbers.py

# Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

 

# Example 1:

# Input: c = 5
# Output: true
# Explanation: 1 * 1 + 2 * 2 = 5
# Example 2:

# Input: c = 3
# Output: false
 

# Constraints:

# 0 <= c <= 2**31 - 1

#Idea: this is two-sum problem


class Solution:       
    def min_num_not_smaller_than_sqrt(self,c):
        left=0
        right=c
        if right*right==c:
            return right
        while left+1<right:
            middle=(left+right)//2
            term=middle*middle
            if term==c:
                # print('2')
                # print(a,middle,c)
                return middle
            elif term>c:
                right=middle
            else:
                left=middle
        return right

    def judgeSquareSum(self, c: int) -> bool:
        #assume a<=b
        a=0
        b=self.min_num_not_smaller_than_sqrt(c)
        while a<=b:
            while a*a+b*b>c:
                b-=1
            if a*a+b*b==c:
                return True
            else:
                a+=1
        return False
    
my_solu=Solution()
print(my_solu.judgeSquareSum(3))
        
