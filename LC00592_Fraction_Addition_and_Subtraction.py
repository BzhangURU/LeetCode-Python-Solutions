# LC00592_Fraction_Addition_and_Subtraction.py

# Given a string expression representing an expression of fraction addition and subtraction, 
# return the calculation result in string format.

# The final result should be an irreducible fraction. If your final result is an integer, 
# change it to the format of a fraction that has a denominator 1. So in this case, 2 should be converted to 2/1.

 

# Example 1:

# Input: expression = "-1/2+1/2"
# Output: "0/1"
# Example 2:

# Input: expression = "-1/2+1/2+1/3"
# Output: "1/3"
# Example 3:

# Input: expression = "1/3-1/2"
# Output: "-1/6"
 

# Constraints:

# The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
# Each fraction (input and output) has the format ±numerator/denominator. If the first 
# input fraction or the output is positive, then '+' will be omitted.
# The input only contains valid irreducible fractions, where the numerator and 
# denominator of each fraction will always be in the range [1, 10]. If the denominator is 1, 
# it means this fraction is actually an integer in a fraction format defined above.
# The number of given fractions will be in the range [1, 10].
# The numerator and denominator of the final result are guaranteed to be valid 
# and in the range of 32-bit int.

# Idea: use numerators (a list) to save all numerators
# use denominators(a list) to save all denominators

class Solution:

    def find_min_common_denominator(self, denominators):
        # denominators is between [1,10]
        #decompose into factors to get denominators
        factors=[0]*8# value factors[v] count the occurence of v. For example, for 8, we set factors[2]=3 
        for i in range(len(denominators)):
            if denominators[i]==1:
                pass#factors[1]=1
            elif denominators[i]==2:
                if factors[2]==0:
                    factors[2]=1
            elif denominators[i]==3:
                if factors[3]==0:
                    factors[3]=1
            elif denominators[i]==4:
                if factors[2]<2:
                    factors[2]=2
            elif denominators[i]==5:
                if factors[5]==0:
                    factors[5]=1
            elif denominators[i]==6:
                if factors[2]==0:
                    factors[2]=1
                if factors[3]==0:
                    factors[3]=1
            elif denominators[i]==7:
                if factors[7]==0:
                    factors[7]=1
            elif denominators[i]==8:
                if factors[2]<3:
                    factors[2]=3
            elif denominators[i]==9:
                if factors[3]<2:
                    factors[3]=2
            elif denominators[i]==10:
                if factors[2]==0:
                    factors[2]=1
                if factors[5]==0:
                    factors[5]=1
            else:
                print(denominators[i])
                raise ValueError
        result=1
        for value in range(8):
            if factors[value]>0:
                result*=value**factors[value]
                # for times in range(factors[value]):
                #     result*=value
        return result


    def get_irreducible_fraction(self, nu, de):
        factor=1
        for v in range(1, de):
            if v*v>de:
                break
            if de%v==0:
                if nu%v==0 and v>factor:
                    factor=v
                re_v=int(de/v)
                if nu%re_v==0 and re_v>factor:
                    factor=re_v

        return int(nu/factor), int(de/factor)


    def fractionAddition(self, expression: str) -> str:
        #first, get numerator and denominator
        if expression[0]=='-':
            my_expression=expression.replace('-','+-')
        else:
            my_expression='+'+expression.replace('-','+-')
        numstr_list=my_expression.split('+')
        #the first element in numstr_list is ''
        num_fractions=len(numstr_list)-1

        numerators=[0]*num_fractions
        denominators=[0]*num_fractions

        for i in range(num_fractions):
            n_d_list=numstr_list[i+1].split('/')
            numerators[i]=int(n_d_list[0])
            denominators[i]=int(n_d_list[1])

        min_common_denominator=self.find_min_common_denominator(denominators)

        sum_numerator=0

        #print(numerators)
        #print(denominators)
        #print(min_common_denominator)

        for i in range(num_fractions):
            sum_numerator+=int(numerators[i]*min_common_denominator/denominators[i])

        result_nu, result_de=self.get_irreducible_fraction(sum_numerator, min_common_denominator)

        return str(result_nu)+'/'+str(result_de)
    
my_class=Solution()
input="-1/2+1/2"

result=my_class.fractionAddition(input)
print(result)

        


        

        
        

