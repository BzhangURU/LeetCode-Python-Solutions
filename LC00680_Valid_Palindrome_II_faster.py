# LC00680_Valid_Palindrome_II_faster.py

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
        
        left=0
        right=len(s)-1

        while left<=right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                break

        if left>right:
            return True
        
        left0=left
        right0=right

        #check delete left
        left=left0+1
        right=right0
        while left<=right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                break
        if left>right:
            return True
        
        #check delete right
        left=left0
        right=right0-1
        while left<=right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                break
        if left>right:
            return True

        return False
    
my_solu=Solution()
s ="aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
my_solu.validPalindrome(s)
        
