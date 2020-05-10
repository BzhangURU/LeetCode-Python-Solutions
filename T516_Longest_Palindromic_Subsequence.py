#https://leetcode.com/problems/longest-palindromic-subsequence/
##Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.
##
##Example 1:
##Input:
##
##"bbbab"
##Output:
##4
##One possible longest palindromic subsequence is "bbbb".
##Example 2:
##Input:
##
##"cbbd"
##Output:
##2
##One possible longest palindromic subsequence is "bb".


def longestPalindromeSubseq(s: str):
    n=len(s)
    dp=[[0 for x in range(n)] for x in range(n)]
    for i in range(n):
        dp[i][i]=1
    for substrLength in range(2,n+1):
        for startIndex in range(0,n-substrLength+1):
            num=max(dp[startIndex][startIndex+substrLength-2],\
                    dp[startIndex+1][startIndex+substrLength-1])
            if s[startIndex]==s[startIndex+substrLength-1]:
                #if substrLength>2:
                num=max(num,2+dp[startIndex+1][startIndex+substrLength-2])
            dp[startIndex][startIndex+substrLength-1]=num
    return dp[0][n-1]
