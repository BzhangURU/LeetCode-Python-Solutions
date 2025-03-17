# LC00629_K_Inverse_Pairs_Array.py

# For an integer array nums, an inverse pair is a pair of integers [i, j] 
# where 0 <= i < j < nums.length and nums[i] > nums[j].

# Given two integers n and k, return the number of different arrays consisting of 
# numbers from 1 to n such that there are exactly k inverse pairs. Since the answer 
# can be huge, return it modulo 10**9 + 7.

 

# Example 1:

# Input: n = 3, k = 0
# Output: 1
# Explanation: Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pairs.
# Example 2:

# Input: n = 3, k = 1
# Output: 2
# Explanation: The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.
 

# Constraints:

# 1 <= n <= 1000
# 0 <= k <= 1000

# Idea: DP, n-1: xxxxx,  n: xxxxxN, N is new largest element
# f(n,k)=
# f(n-1,k) xxxxxN +
# f(n-1,k-1) xxxxNx +
# f(n-1,k-2) xxxNxx (Nxx will form two new inverse pairs) +
# f(n-1,k-(n-1)) Nxxxxx

# K=k+1
# f(n,K)=f(n,K-1)+f(n-1,K)-f(n-1,K-n)

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        if n==1:
            if k==0:
                return 1
            else:
                return 0
        
        dp=[[0 for c in range(k+1)] for r in range(n+1)]

        dp[2][0]=1
        if k>=1:
            dp[2][1]=1
        if k>=2:
            for c in range(2,k+1):
                dp[2][c]=0
        if n==2:
            return dp[n][k]
        
        for r in range(3,n+1):
            dp[r][0]=1
            for c in range(1,k+1):
                dp[r][c]=dp[r][c-1]+dp[r-1][c]
                if c>=r:
                    dp[r][c]-=dp[r-1][c-r]
                dp[r][c]=dp[r][c]%(10**9+7)

        return dp[n][k]


            
        

