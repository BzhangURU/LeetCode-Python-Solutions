# LC00470_Implement_Rand10_Using_Rand7_faster.py
# Given the API rand7() that generates a uniform random integer in the range [1, 7], 
# write a function rand10() that generates a uniform random integer in the range [1, 10]. 
# You can only call the API rand7(), and you shouldn't call any other API. Please do not '
# 'use a language's built-in random API.

# Each test case will have one internal argument n, the number of times that your implemented 
# function rand10() will be called while testing. Note that this is not an argument passed to rand10().

# Example 1:

# Input: n = 1
# Output: [2]
# Example 2:

# Input: n = 2
# Output: [2,8]
# Example 3:

# Input: n = 3
# Output: [3,8,10]
 

# Constraints:

# 1 <= n <= 105
 

# Follow up:

# What is the expected value for the number of calls to rand7() function?
# Could you minimize the number of calls to rand7()?

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

# Idea: we use rand7 to generate large numbers, then save it for next use.
# 7**6=117649, get a number below 100000, then use it 5 times
    
def generate_a_num_by_rand7_6_times():
    num=0
    for i in range(6):
        num=7*num+(rand7()-1)
    return num

class Solution:
    number=0
    leftover_times=0
    def rand10(self):
        """
        :rtype: int
        """
        if self.leftover_times==0:
            self.number=generate_a_num_by_rand7_6_times()
            while self.number >=100000:
                self.number=generate_a_num_by_rand7_6_times()
            self.leftover_times=5

        self.leftover_times-=1
        result=self.number%10+1
        self.number=self.number//10
        return result

        
       



        
