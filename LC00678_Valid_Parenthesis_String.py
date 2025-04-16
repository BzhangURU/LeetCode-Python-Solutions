# LC00678_Valid_Parenthesis_String.py

# Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

# The following rules define a valid string:

# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "(*)"
# Output: true
# Example 3:

# Input: s = "(*))"
# Output: true
 

# Constraints:

# 1 <= s.length <= 100
# s[i] is '(', ')' or '*'.

# idea: iterate all chars, keep tracking extra_left_range_max, extra_left_range_min

class Solution:
    def checkValidString(self, s: str) -> bool:
        extra_left_range_max=0
        extra_left_range_min=0
        for i in range(len(s)):
            if s[i]=='(':
                extra_left_range_max+=1
                extra_left_range_min+=1
            elif s[i]==')':
                if extra_left_range_max<=0:
                    return False
                else:
                    extra_left_range_max-=1
                    extra_left_range_min=max(0,extra_left_range_min-1)
            else:
                if extra_left_range_max==0:#0,0
                    #has to be left or empty
                    extra_left_range_max+=1
                elif extra_left_range_min==0:#5,0
                    extra_left_range_max+=1
                else:#8,3
                    extra_left_range_max+=1
                    extra_left_range_min-=1

        if extra_left_range_min>0:
            return False
        
        return True
