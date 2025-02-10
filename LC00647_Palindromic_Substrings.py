# LC00647_Palindromic_Substrings.py

# Given a string s, return the number of palindromic substrings in it.

# A string is a palindrome when it reads the same backward as forward.

# A substring is a contiguous sequence of characters within the string.

 

# Example 1:

# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:

# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

# Constraints:

# 1 <= s.length <= 1000
# s consists of lowercase English letters.

#Idea: we first iterate and fix the center of palindrom, and cound the number palindroms whose center is current center.

class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s)==0:
            return 0
        
        result=0
        for i in range(len(s)):
            center=i
            for offset in range(0,min(len(s)-1-center+1,center-0+1)):
                if s[center-offset]==s[center+offset]:
                    result+=1
                else:
                    break
            #center is between i and i+1    
            for offset in range(1,min(len(s)-1-center+1,center-0+2)):
                if s[center+1-offset]==s[center+offset]:
                    result+=1
                else:
                    break
        return result
        
