# LC00518_Coin_Change_2.py

# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

# You may assume that you have an infinite number of each kind of coin.

# The answer is guaranteed to fit into a signed 32-bit integer.

 

# Example 1:

# Input: amount = 5, coins = [1,2,5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
# Example 2:

# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
# Example 3:

# Input: amount = 10, coins = [10]
# Output: 1
 

# Constraints:

# 1 <= coins.length <= 300
# 1 <= coins[i] <= 5000
# All the values of coins are unique.
# 0 <= amount <= 5000



# follow the existing algorithm in https://leetcode.com/problems/coin-change-ii/description/:
# If we want to make change for N cents, and we have infinite supply of each of {S = S_1, S_2, ..., S_m} valued coins.

# The set of solutions for this problem, C(m, N), can be partitioned into two sets.

# There are those sets that do not contain any S_m and
# Those sets that contain at least 1 S_m
# Then we get recurence relation.
# C(m, N) = C(m-1, N) + C(m, N - S_m)

def get_DP_value(DP, r, c):
    if c<0:
        return 0
    elif c==0:
        return 1
    else:
        return DP[r][c]

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        num_coin_type=len(coins)
        DP=[[0 for _ in range(amount+1)] for _ in range(num_coin_type+1)]

        #m=1
        r=1
        for c in range(amount+1):
            if c%coins[r-1]==0:
                DP[1][c]=1

        for r in range(2, num_coin_type+1):
            for c in range(amount+1):
                if c==0:
                    DP[r][c]=1
                else:
                    DP[r][c]=DP[r-1][c]+get_DP_value(DP,r,c-coins[r-1])

        return DP[num_coin_type][amount]
