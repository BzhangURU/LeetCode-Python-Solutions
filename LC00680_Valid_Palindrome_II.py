# LC00680_Valid_Palindrome_II.py

# Given a string s, return true if the s can be palindrome after deleting at most one character from it.


# Example 1:

# Input: s = "aba"
# Output: true
# Example 2:

# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:

# Input: s = "abc"
# Output: false
 

# Constraints:

# 1 <= s.length <= 10**5
# s consists of lowercase English letters.

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s)<=2:
            return True
        
        delete_left_side_success=True
        delete_right_side_success=True
        deletion_times=0
        left=0
        right=len(s)-1

        while left<=right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                left+=1
                deletion_times+=1

            if deletion_times>1:
                delete_left_side_success=False
                break
            
        deletion_times=0
        left=0
        right=len(s)-1

        while left<=right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                right-=1
                deletion_times+=1

            if deletion_times>1:
                delete_right_side_success=False
                break
        if delete_left_side_success==False and delete_right_side_success==False:
            return False
            
        return True
        
