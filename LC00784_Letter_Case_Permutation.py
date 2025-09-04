# LC00784_Letter_Case_Permutation.py

# Given a string s, you can transform every letter individually to be lowercase or 
# uppercase to create another string.

# Return a list of all possible strings we could create. Return the output in any order.

 

# Example 1:

# Input: s = "a1b2"
# Output: ["a1b2","a1B2","A1b2","A1B2"]
# Example 2:

# Input: s = "3z4"
# Output: ["3z4","3Z4"]
 

# Constraints:

# 1 <= s.length <= 12
# s consists of lowercase English letters, uppercase English letters, and digits.


# Idea: iteration each char in string, duplicate the output list if it is English letter, simply append if it is digit.

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        output_list=['']
        for i in range(len(s)):
            if ord(s[i])>=ord('0') and ord(s[i])<=ord('9'):
                #add digit to all elements in the output list. 
                for j in range(len(output_list)):
                    output_list[j]=output_list[j]+s[i]
            else:
                original_len=len(output_list)
                for j in range(original_len):
                    original_element=output_list[j]
                    output_list[j]=original_element+s[i].lower()
                    output_list.append(original_element+s[i].upper())
        return output_list

        



