# LC00667_Beautiful_Arrangement_II.py

# Given two integers n and k, construct a list answer that contains n different 
# positive integers ranging from 1 to n and obeys the following requirement:

# Suppose this list is answer = [a1, a2, a3, ... , an], then the list [|a1 - a2|, 
#             |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.
# Return the list answer. If there multiple valid answers, return any of them.

 

# Example 1:

# Input: n = 3, k = 1
# Output: [1,2,3]
# Explanation: The [1,2,3] has three different positive integers ranging from 1 to 3, 
# and the [1,1] has exactly 1 distinct integer: 1
# Example 2:

# Input: n = 3, k = 2
# Output: [1,3,2]
# Explanation: The [1,3,2] has three different positive integers ranging from 1 to 3, 
# and the [2,1] has exactly 2 distinct integers: 1 and 2.
 

# Constraints:

# 1 <= k < n <= 10**4


# Idea: for example,if k==9, then we set to have 1,2,3,....,9, list first (k+1) nums first
# so we first list: 1,10,2,9,3,8,4,7,5,6, then if we have remaining numbers,
# we list 1,10,2,9,3,8,4,7,5,6, 11,12,13,14,15,16,...

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        result=[]
        for i in range(k+1):
            if i&1==0:
                result.append((i//2)+1)
            else:
                result.append(k+1-i//2)
        for i in range(k+1,n):
            result.append(i+1)
        return result
