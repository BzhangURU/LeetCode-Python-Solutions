# LC00696_Count_Binary_Substrings.py

# Given a binary string s, return the number of non-empty substrings that have 
# the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

# Substrings that occur multiple times are counted the number of times they occur.

 

# Example 1:

# Input: s = "00110011"
# Output: 6
# Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: 
# "0011", "01", "1100", "10", "0011", and "01".
# Notice that some of these substrings repeat and are counted the number of times they occur.
# Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
# Example 2:

# Input: s = "10101"
# Output: 4
# Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of 
# consecutive 1's and 0's.
 

# Constraints:

# 1 <= s.length <= 10**5
# s[i] is either '0' or '1'.

# Hint: How many valid binary substrings exist in "000111", and how many in "11100"? What about "00011100"?

# Idea: iterate, when there is transition like 01 and 10, spread to both sides to count 

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        result=0
        for i in range(1,len(s)):
            if s[i-1]!=s[i]:
                j=1
                while i-1-j>=0 and i+j<len(s) and s[i-1-j]==s[i-1] and s[i]==s[i+j]:
                    j+=1
                result+=j
        return result



        


