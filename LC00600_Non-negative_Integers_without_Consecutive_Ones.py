# LC00600_Non-negative_Integers_without_Consecutive_Ones.py

# Given a positive integer n, return the number of the integers in the range [0, n] 
# whose binary representations do not contain consecutive ones.

 

# Example 1:

# Input: n = 5
# Output: 5
# Explanation:
# Here are the non-negative integers <= 5 with their corresponding binary 
# representations:
# 0 : 0
# 1 : 1
# 2 : 10
# 3 : 11
# 4 : 100
# 5 : 101
# Among them, only integer 3 disobeys the rule (two consecutive ones) and 
# the other 5 satisfy the rule. 
# Example 2:

# Input: n = 1
# Output: 2
# Example 3:

# Input: n = 2
# Output: 3
 

# Constraints:

# 1 <= n <= 10**9

# My Idea: set FixDigits(n) as the number of qualified integers with 1xxx...xxx format, 
# where the total num of digits is n, "x" can be either 0 or 1. FixDigits(0)=1---> the number is "0"
# Then FixDigits(5)= 1xxxx = 10xxx = 101xx + 100xx, where 100xx = 1001x + 1000x, where 1000x = 10001 + 10000
# So  FixDigits(5)=FixDigits(3)+FixDigits(2)+FixDigits(1)+FixDigits(0)

# So if number is   10 110, then findIntegers(10110)=FixDigits(4)+FixDigits(3)+FixDigits(2)+FixDigits(1)+FixDigits(0)+findIntegers(110)
# if number is      11 101, then findIntegers(11101)=findIntegers(10111)=FixDigits(4)+FixDigits(3)+FixDigits(2)+FixDigits(1)+FixDigits(0)+findIntegers(111)
#                           =FixDigits(4)+FixDigits(3)+FixDigits(2)+FixDigits(1)+FixDigits(0)   +   FixDigits(3)+FixDigits(2)+FixDigits(1)+FixDigits(0)
#                           =FixDigits(6)+FixDigits(5)

# So first, we calculate FixDigits, then follow the above formula to calculate. 




class Solution:
    def DP_find_integers(self, FixDigits, binary_list):
        # binary_list is like [1,1,1,0,1]
        if len(binary_list)==1:
            if binary_list[0]==0:
                return 1
            elif binary_list[0]==1:
                return 2
            
        
        #   binary_list[0] is always 1
        if binary_list[1]==1:
            #first two elements are 1 and 1
            return FixDigits[len(binary_list)+1]+FixDigits[len(binary_list)]
        else:
            #first two elements are 1 and 0, find the next 1
            index=1
            while index<len(binary_list) and binary_list[index]!=1:
                index+=1
            if index==len(binary_list):
                #10000
                return FixDigits[len(binary_list)+1]+1
            else:
                num_digits=len(binary_list)
                binary_list[0:index]=[]
                return FixDigits[num_digits+1]+self.DP_find_integers(FixDigits,binary_list)


        
        


    def findIntegers(self, n: int) -> int:
        if n==0:
            return 1
        elif n==1:
            return 2
        
        #change n to binary_list
        binary_list=[]
        while n!=0:
            binary_list.append(n%2)
            n=n//2
        binary_list.reverse()

        num_digits=len(binary_list)

        #calculate FixDigits
        FixDigits=[0]*(num_digits+2)

        FixDigits[0]=1
        FixDigits[1]=1

        for i in range(2,(num_digits+2)):
            my_sum=0
            for j in range(0,i-1):
                my_sum+=FixDigits[j]
            FixDigits[i]=my_sum

        return self.DP_find_integers(FixDigits, binary_list)

        
        
my_solu=Solution()
my_solu.findIntegers(5)
        



