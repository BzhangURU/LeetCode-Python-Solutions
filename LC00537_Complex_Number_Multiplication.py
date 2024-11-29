# LC00537_Complex_Number_Multiplication.py

# A complex number can be represented as a string on the form "real+imaginaryi" where:

# real is the real part and is an integer in the range [-100, 100].
# imaginary is the imaginary part and is an integer in the range [-100, 100].
# i2 == -1.
# Given two complex numbers num1 and num2 as strings, return a string of the complex number that represents their multiplications.

 

# Example 1:

# Input: num1 = "1+1i", num2 = "1+1i"
# Output: "0+2i"
# Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
# Example 2:

# Input: num1 = "1+-1i", num2 = "1+-1i"
# Output: "0+-2i"
# Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
 

# Constraints:

# num1 and num2 are valid complex numbers.


class Solution:
    def get_two_parts(self,num_str):
        index_plus=num_str.find('+')
        index_i=num_str.find('i')
        real=int(num_str[0:index_plus])
        imaginary=int(num_str[index_plus+1:index_i])
        return real, imaginary
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        #(a+bi)x(c+di)=ac+bci+adi-bd=(ac-bd)+(bc+ad)i

        num1_real, num1_imaginary = self.get_two_parts(num1)
        num2_real, num2_imaginary = self.get_two_parts(num2)

        answer= str(num1_real*num2_real-num1_imaginary*num2_imaginary)+'+'+str(num1_imaginary*num2_real+num1_real*num2_imaginary)+'i'

        return answer
