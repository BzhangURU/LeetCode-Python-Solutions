# LC00392_Is_Subsequence.py

# Given two strings s and t, return true if s is a subsequence of t, 
# or false otherwise.

# A subsequence of a string is a new string that is formed from the 
# original string by deleting some (can be none) of the characters 
# without disturbing the relative positions of the remaining characters. 
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false
 

# Constraints:

# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.
 

# Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk 
# where k >= 10**9, and you want to check one by one to see if t has its subsequence. 
# In this scenario, how would you change your code?


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)>len(t):
            return False
        elif len(s)==len(t):
            if s==t:
                return True
            else:
                return False
        elif len(s)==0:
            return True
        
        ind_s=0
        for ind_t in range(len(t)):
            if t[ind_t]==s[ind_s]:
                ind_s+=1
                if ind_s==len(s):
                    return True
                elif len(s)-ind_s>len(t)-ind_t-1:
                    return False
        return False
