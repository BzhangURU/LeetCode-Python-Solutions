# LC00664_Strange_Printer.py

# There is a strange printer with the following two special properties:

# The printer can only print a sequence of the same character each time.
# At each turn, the printer can print new characters starting from and ending at 
# any place and will cover the original existing characters.
# Given a string s, return the minimum number of turns the printer needed to print it.

 

# Example 1:

# Input: s = "aaabbb"
# Output: 2
# Explanation: Print "aaa" first and then print "bbb".
# Example 2:

# Input: s = "aba"
# Output: 2
# Explanation: Print "aaa" first and then print "b" from the second place of the string, 
# which will cover the existing character 'a'.
 

# Constraints:

# 1 <= s.length <= 100
# s consists of lowercase English letters.

# Idea: Use DP. First, shrink string from "aaabbbbbbccd" to "abcd",
#  Set f(start, end) as result, then f(start, start)=1,

# if s[i]==s[j], then dp[i][j]==dp[i][j-1].
# if s[end-1] is 'a', and between start and end-1, loc1,loc2,loc3 has 'a'
# f(start, end)=min( f(start, end-1)+1 ,  f(start, loc1-1)+f(loc1+1,end-1), ...




class Solution:
    def strangePrinter(self, s: str) -> int:
        
        s_short_list=[s[0]]

        for i in range(1,len(s)):
            if s[i]!=s[i-1]:
                s_short_list.append(s[i])

        s_short=''.join(s_short_list)

        dp=[[-1 for ending in range(len(s_short))] for start in range(len(s_short))]

        for i in range(len(s_short)):
            dp[i][i]=1

        for offset in range(1,len(s_short)):
            for start in range(0, len(s_short)-offset):
                dp[start][start+offset]=dp[start][start+offset-1]+1
                for i in range(start, start+offset):
                    if s_short[i]==s_short[start+offset]:
                        if i>start and dp[start][i-1]+dp[i][start+offset-1]<dp[start][start+offset]:
                            dp[start][start+offset]=dp[start][i-1]+dp[i][start+offset-1]
                        elif i==start and dp[start][start+offset-1]<dp[start][start+offset]:
                            dp[start][start+offset]=dp[start][start+offset-1]

        return dp[0][len(s_short)-1]
        



