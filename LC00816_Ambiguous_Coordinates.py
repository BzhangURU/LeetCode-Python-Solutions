# LC00816_Ambiguous_Coordinates.py

# We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)". 
# Then, we removed all commas, decimal points, and spaces and ended up with the string s.

# For example, "(1, 3)" becomes s = "(13)" and "(2, 0.5)" becomes s = "(205)".
# Return a list of strings representing all possibilities for what our original coordinates could have been.

# Our original representation never had extraneous zeroes, 
# so we never started with numbers like "00", "0.0", "0.00", "1.0", "001", "00.01", 
# or any other number that can be represented with fewer digits. 
# Also, a decimal point within a number never occurs without at least one digit occurring before it, 
# so we never started with numbers like ".1".

# The final answer list can be returned in any order. All coordinates in 
# the final answer have exactly one space between them (occurring after the comma.)

 

# Example 1:

# Input: s = "(123)"
# Output: ["(1, 2.3)","(1, 23)","(1.2, 3)","(12, 3)"]
# Example 2:

# Input: s = "(0123)"
# Output: ["(0, 1.23)","(0, 12.3)","(0, 123)","(0.1, 2.3)","(0.1, 23)","(0.12, 3)"]
# Explanation: 0.0, 00, 0001 or 00.01 are not allowed.
# Example 3:

# Input: s = "(00011)"
# Output: ["(0, 0.011)","(0.001, 1)"]
 

# Constraints:

# 4 <= s.length <= 12
# s[0] == '(' and s[s.length - 1] == ')'.
# The rest of s are digits.

from typing import List

class Solution:
    def get_num_options(self,first_num_digits):
        first_num_options=[]
        #rule: the last digit can't be zero if there is decimal part
        #rule: the first digit can't be zero unless like 0.X
        if first_num_digits[0]=='0':
            if len(first_num_digits)==1:
                first_num_options.append('0')
            elif first_num_digits[-1]=='0':
                return []
            else:
                first_num_options.append('0.'+first_num_digits[1:])
        else:
            first_num_options.append(first_num_digits)
            if first_num_digits[-1]!='0':
                for point_ind in range(0,len(first_num_digits)-1):
                    #print(f'point_ind={point_ind}')
                    #print(first_num_digits[0:point_ind+1]+'.'+first_num_digits[point_ind+1:len(first_num_digits)])
                    first_num_options.append(first_num_digits[0:point_ind+1]+'.'+first_num_digits[point_ind+1:len(first_num_digits)])
        return first_num_options

    def ambiguousCoordinates(self, s: str) -> List[str]:
        output=[]
        for last_num_ind in range(1,len(s)-2):
            
            first_num_digits=s[1:last_num_ind+1]
            first_num_options=self.get_num_options(first_num_digits)

            second_num_digits=s[last_num_ind+1:len(s)-1]
            second_num_options=self.get_num_options(second_num_digits)

            #print(first_num_options)
            #print(second_num_options)
            #print('')

            for first_num in first_num_options:
                for second_num in second_num_options:
                    output.append('('+first_num+', '+second_num+')')
        return output

s="(123)"
my_solu=Solution()
my_solu.ambiguousCoordinates(s) 

        


