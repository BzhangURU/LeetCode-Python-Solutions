# LC00679_24_Game.py

# You are given an integer array cards of length 4. You have four cards, each containing 
# a number in the range [1, 9]. You should arrange the numbers on these cards in 
# a mathematical expression using the operators ['+', '-', '*', '/'] and the 
# parentheses '(' and ')' to get the value 24.

# You are restricted with the following rules:

# The division operator '/' represents real division, not integer division.
# For example, 4 / (1 - 2 / 3) = 4 / (1 / 3) = 12.
# Every operation done is between two numbers. In particular, we cannot use '-' as a unary operator.
# For example, if cards = [1, 1, 1, 1], the expression "-1 - 1 - 1 - 1" is not allowed.
# You cannot concatenate numbers together
# For example, if cards = [1, 2, 1, 2], the expression "12 + 12" is not valid.
# Return true if you can get such expression that evaluates to 24, and false otherwise.

 

# Example 1:

# Input: cards = [4,1,8,7]
# Output: true
# Explanation: (8-4) * (7-1) = 24
# Example 2:

# Input: cards = [1,2,1,2]
# Output: false
 

# Constraints:

# cards.length == 4
# 1 <= cards[i] <= 9

# Idea: define a function, two inputs, each input is a set of numbers, output is also a set of numbers

def get_largest_common_divisor(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def get_possible_outputs(set1, set2, output_set, try_plus=True):
    for num1 in set1:
        for num2 in set2:
            num1_nu=num1[0]
            num1_de=num1[1]
            num2_nu=num2[0]
            num2_de=num2[1]

            if try_plus:
                #try plus
                output_nu=num1_nu*num2_de+num2_nu*num1_de
                output_de=num1_de*num2_de
                lcd=get_largest_common_divisor(output_nu,output_de)
                output_nu/=lcd
                output_de/=lcd
                output_set.add((output_nu,output_de))

            #try minus
            output_nu=num1_nu*num2_de-num2_nu*num1_de
            output_de=num1_de*num2_de
            lcd=get_largest_common_divisor(output_nu,output_de)
            output_nu/=lcd
            output_de/=lcd
            output_set.add((output_nu,output_de))

            #try multiply
            output_nu=num1_nu*num2_nu
            output_de=num1_de*num2_de
            lcd=get_largest_common_divisor(output_nu,output_de)
            output_nu/=lcd
            output_de/=lcd
            output_set.add((output_nu,output_de))

            #try division
            if num2_nu!=0:
                output_nu=num1_nu*num2_de
                output_de=num1_de*num2_nu
                lcd=get_largest_common_divisor(output_nu,output_de)
                output_nu/=lcd
                output_de/=lcd
                output_set.add((output_nu,output_de))

class Solution:
    def possible_outputs(self, input1_set, input2_set):
        output_set=set()
        get_possible_outputs(input1_set,input2_set,output_set)
        get_possible_outputs(input2_set,input1_set,output_set,try_plus=False)
        return output_set

    def judgePoint24(self, cards: List[int]) -> bool:
        result_set=set()
        for o1 in range(4):
            for o2 in range(4):
                if o2!=o1:
                    for o3 in range(4):
                        if o3!=o2 and o3!=o1:
                            for o4 in range(4):
                                if o4!=o3 and o4!=o2 and o4!=o1:
                                    set_o1=set([(cards[o1],1)])
                                    set_o2=set([(cards[o2],1)])
                                    set_o3=set([(cards[o3],1)])
                                    set_o4=set([(cards[o4],1)])

                                    set_12=self.possible_outputs(set_o1,set_o2)
                                    set_123=self.possible_outputs(set_12,set_o3)
                                    set_1234=self.possible_outputs(set_123,set_o4)
                                    result_set=result_set | set_1234
                                    if (24,1) in result_set:
                                        return True
                                    
                                    set_34=self.possible_outputs(set_o3,set_o4)
                                    set_12_34=self.possible_outputs(set_12,set_34)
                                    result_set=result_set | set_12_34
                                    if (24,1) in result_set:
                                        return True
        return False
                                    



