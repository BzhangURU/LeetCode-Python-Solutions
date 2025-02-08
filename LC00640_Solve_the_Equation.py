# LC00640_Solve_the_Equation.py

# Solve a given equation and return the value of 'x' in the form of a string "x=#value". The equation contains only '+', '-' operation, the variable 'x' and its coefficient. You should return "No solution" if there is no solution for the equation, or "Infinite solutions" if there are infinite solutions for the equation.

# If there is exactly one solution for the equation, we ensure that the value of 'x' is an integer.

 

# Example 1:

# Input: equation = "x+5-3+x=6+x-2"
# Output: "x=2"
# Example 2:

# Input: equation = "x=x"
# Output: "Infinite solutions"
# Example 3:

# Input: equation = "2x=x"
# Output: "x=0"
 

# Constraints:

# 3 <= equation.length <= 1000
# equation has exactly one '='.
# equation consists of integers with an absolute value in the range [0, 100] without any leading zeros, and the variable 'x'.
# The input is generated that if there is a single solution, it will be an integer.

# Idea: count number of x on left side of "=" and on right side of equation.
# get sum of constant left to "=" and right to "="
# if x has coefficient, add "*"

def this_char_is_a_number(a_char):
    if ord(a_char)>=ord('0') and ord(a_char)<=ord('9'):
        return True
    else:
        return False
    
def get_coefficient_const(left_part):
    left_part=left_part.replace('-','+-')
    left_list=left_part.split('+')
    if left_list[0]=='':
        del left_list[0]
    # first element may be empty string
    # ['', '3x', '5', '-3', 'x', '-x', '-2x']
    left_const_sum=0
    left_x_coef=0
    #print(left_list)
    for i in range(0,len(left_list)):
        find_x_ind=left_list[i].find('x')
        if find_x_ind<0:
            #normal number 
            left_const_sum+=int(left_list[i])
        else:
            # has x
            if left_list[i]=='x':
                left_x_coef+=1
            elif left_list[i]=='-x':
                left_x_coef-=1
            else:
                coef=left_list[i].replace('x','')
                left_x_coef+=int(coef)
    return left_x_coef, left_const_sum

class Solution:
    def solveEquation(self, equation: str) -> str:
        two_parts=equation.split('=')
        left_part=two_parts[0]
        right_part=two_parts[1]

        
        left_x_coef, left_const_sum = get_coefficient_const(left_part)
        right_x_coef, right_const_sum = get_coefficient_const(right_part)
        #print('left', left_x_coef, left_const_sum)
        #print('right', right_x_coef, right_const_sum)

        if left_x_coef==right_x_coef:
            if left_const_sum==right_const_sum:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            return "x="+str((right_const_sum-left_const_sum)//(left_x_coef-right_x_coef))

my_solu=Solution()

equation="-x=-1"
print(my_solu.solveEquation(equation))

