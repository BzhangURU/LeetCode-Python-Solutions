# LC00726_Number_of_Atoms.py

# Given a string formula representing a chemical formula, return the count of each atom.

# The atomic element always starts with an uppercase character, 
# then zero or more lowercase letters, representing the name.

# One or more digits representing that element's count may follow if the count is greater than 1. 
# If the count is 1, no digits will follow.

# For example, "H2O" and "H2O2" are possible, but "H1O2" is impossible.
# Two formulas are concatenated together to produce another formula.

# For example, "H2O2He3Mg4" is also a formula.
# A formula placed in parentheses, and a count (optionally added) is also a formula.

# For example, "(H2O2)" and "(H2O2)3" are formulas.
# Return the count of all elements as a string in the following form: the first name (in sorted order), 
# followed by its count (if that count is more than 1), followed by the second name (in sorted order), 
# followed by its count (if that count is more than 1), and so on.

# The test cases are generated so that all the values in the output fit in a 32-bit integer.

 

# Example 1:

# Input: formula = "H2O"
# Output: "H2O"
# Explanation: The count of elements are {'H': 2, 'O': 1}.
# Example 2:

# Input: formula = "Mg(OH)2"
# Output: "H2MgO2"
# Explanation: The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
# Example 3:

# Input: formula = "K4(ON(SO3)2)2"
# Output: "K4N2O14S4"
# Explanation: The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
 

# Constraints:

# 1 <= formula.length <= 1000
# formula consists of English letters, digits, '(', and ')'.
# formula is always valid.

# Idea: first decode the string "Mg(OH)2" as "Mg ( O H ) 2"
# then, use a list like [(Mg, 1), (O,1), ...] to save information, use a stack to save 
# the location 'loc' of left bracket (we record the index of first element after the saved left breacket in the created list)
# then if we have a right bracket, then we pop in stack, and multiply all counts between 'loc' and current place.
from collections import deque
class Solution:
    def charType(self,my_char):
        if ord(my_char)>=ord('a') and ord(my_char)<=ord('z'):
            return 4
        elif ord(my_char)>=ord('A') and ord(my_char)<=ord('Z'):
            return 0
        elif ord(my_char)>=ord('0') and ord(my_char)<=ord('9'):
            return 1
        elif my_char=='(':
            return 2
        elif my_char==')':
            return 3
        else:
            raise ValueError(f'Invalid character: {my_char}')
    def countOfAtoms(self, formula: str) -> str:
        char_list=[]
        last_char_type=-1#formula: "Mg(OH)2"
        for i in range(len(formula)):
            new_char=formula[i]
            cur_char_type=self.charType(new_char)
            if (cur_char_type!=last_char_type or cur_char_type==0 or cur_char_type==2 or cur_char_type==3) and i!=0:
                if not cur_char_type==4:
                    char_list.append('/')

            char_list.append(new_char)
            
            #if new_char=='N':
            #    last_char_type=last_char_type
            
            last_char_type=cur_char_type

        # char_list will be like ["M" ,"g", "/", "(", "/", "O", "/", "H", "/", ")", "/", "2"]
        #print(char_list)

        new_formula=''.join(char_list)
        element_list=new_formula.split('/') #element_list will be like ["Mg", "(", "O", "H", ")", "2"]

        #print(element_list)

        count_list=[]
        my_q=deque()
        last_right_bracket_place=-5
        poped_left_bracket_place=-5
        for i,element in enumerate(element_list):
            char_type=self.charType(element[0])
            if char_type==0:
                count_list.append([element,1])
            elif char_type==2:#'('
                my_q.append(len(count_list))
            elif char_type==1:
                if last_right_bracket_place<i-1:
                    count_list[-1][1]*=int(element)
                else:
                    multiple=int(element)
                    for j in range(poped_left_bracket_place,len(count_list)):
                        count_list[j][1]*=multiple


            elif char_type==3:#')'
                last_right_bracket_place=i
                poped_left_bracket_place=my_q.pop()
                #for j in range(first_index,len(count_list)):

        #put to dictionary to merge same Atoms
        my_dict={}
        for i, element in enumerate(count_list):
            if element[0] not in my_dict:
                my_dict[element[0]]=element[1]
            else:
                my_dict[element[0]]+=element[1]

        #put to list again
        output_list=[]
        for k,v in my_dict.items():
            output_list.append((k,v))
        output_list.sort(key=lambda p: p[0])

        output_charStr_list=[]
        for i,element in enumerate(output_list):
            output_charStr_list.append(element[0])
            if element[1]!=1:
                output_charStr_list.append(str(element[1]))

        output_str=''.join(output_charStr_list)
        return output_str


            


#formula = "K4(ON(SO3)2)2"
formula="((HHe28Be26He)9)34"
my_solu=Solution()
print(my_solu.countOfAtoms(formula))


