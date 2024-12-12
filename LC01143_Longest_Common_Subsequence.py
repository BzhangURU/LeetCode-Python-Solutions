# LC01143_Longest_Common_Subsequence.py

# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

 

# Example 1:

# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.
# Example 2:

# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
# Example 3:

# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
 

# Constraints:

# 1 <= text1.length, text2.length <= 1000
# text1 and text2 consist of only lowercase English characters.

# Hint: Try dynamic programming. DP[i][j] represents the longest common subsequence of text1[0 ... i] & text2[0 ... j].
# Hint: DP[i][j] = DP[i - 1][j - 1] + 1 , if text1[i] == text2[j] DP[i][j] = max(DP[i - 1][j], DP[i][j - 1]) , otherwise

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        DP=[[0 for _ in range(len(text2))] for _ in range(len(text1))]
        if text1[0]==text2[0]:
            DP[0][0]=1
            if len(text1)>1:
                DP[1][0]=1
            if len(text2)>1:
                DP[0][1]=1

        if len(text1)>1:
            if text1[1]==text2[0]:
                DP[1][0]=1

        if len(text2)>1:
            if text1[0]==text2[1]:
                DP[0][1]=1

        for i in range(len(text1)):
            for j in range(len(text2)):
                if i+j>=2:
                    if text1[i]==text2[j]:
                        if i>=1 and j>=1:
                            DP[i][j]=DP[i-1][j-1]+1
                        else:
                            DP[i][j]=1
                    else:
                        if i==0:
                            DP[i][j]=DP[i][j - 1]
                        elif j==0:
                            DP[i][j]=DP[i-1][j]
                        else:
                            DP[i][j]=max(DP[i - 1][j], DP[i][j - 1])

        return DP[len(text1)-1][len(text2)-1]
