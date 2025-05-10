# LC00712_Minimum_ASCII_Delete_Sum_for_Two_Strings.py

# Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.

 

# Example 1:

# Input: s1 = "sea", s2 = "eat"
# Output: 231
# Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
# Deleting "t" from "eat" adds 116 to the sum.
# At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
# Example 2:

# Input: s1 = "delete", s2 = "leet"
# Output: 403
# Explanation: Deleting "dee" from "delete" to turn the string into "let",
# adds 100[d] + 101[e] + 101[e] to the sum.
# Deleting "e" from "leet" adds 101[e] to the sum.
# At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
# If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
 

# Constraints:

# 1 <= s1.length, s2.length <= 1000
# s1 and s2 consist of lowercase English letters.

# Hint: Let dp(i, j) be the answer for inputs s1[i:] and s2[j:].

# Idea: Let dp(i, j) be the answer for inputs s1[:i] and s2[:j].
# if s1[i]!=s2[j]:
#       dp(i+1, j+1)= min( dp(i,j+1)+chr(s1[i]) ,dp(i+1,j)+chr(s2[j])  )
# else:
#       dp(i+1, j+1)= dp(i,j)


class Solution:


    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp=[[-1 for c in range(len(s2)+1)] for r in range(len(s1)+1)]

        dp[0][0]=0
        for c in range(1, len(s2)+1):
            dp[0][c]=dp[0][c-1]+ord(s2[c-1])

        for r in range(1,len(s1)+1):
            dp[r][0]=dp[r-1][0]+ord(s1[r-1])


        for r in range(1,len(s1)+1):
            for c in range(1,len(s2)+1):
                if s1[r-1]!=s2[c-1]:
                    dp[r][c]= min( dp[r-1][c]+ord(s1[r-1]) ,dp[r][c-1]+ord(s2[c-1])  )
                else:
                    dp[r][c]= dp[r-1][c-1]

        return dp[len(s1)][len(s2)]
