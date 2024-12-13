# LC00583_Delete_Operation_for_Two_Strings.py

# Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

# In one step, you can delete exactly one character in either string.

 

# Example 1:

# Input: word1 = "sea", word2 = "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
# Example 2:

# Input: word1 = "leetcode", word2 = "etco"
# Output: 4
 

# Constraints:

# 1 <= word1.length, word2.length <= 500
# word1 and word2 consist of only lowercase English letters.

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

    def minDistance(self, word1: str, word2: str) -> int:
        return len(word1)+len(word2)-2*self.longestCommonSubsequence(word1, word2)
