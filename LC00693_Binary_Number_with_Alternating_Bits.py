# LC00693_Binary_Number_with_Alternating_Bits.py

# Given a positive integer, check whether it has alternating bits: namely, 
# if two adjacent bits will always have different values.

 

# Example 1:

# Input: n = 5
# Output: true
# Explanation: The binary representation of 5 is: 101
# Example 2:

# Input: n = 7
# Output: false
# Explanation: The binary representation of 7 is: 111.
# Example 3:

# Input: n = 11
# Output: false
# Explanation: The binary representation of 11 is: 1011.
 

# Constraints:

# 1 <= n <= 2**31 - 1

# Idea: 
# n_r1=n>>1
# (n & n_r1)==0 requires that the 1s has no adjacent 1s. 
# (((n | n_r1)+1) & n)==0 requires that (n | n_r1)+1 must increase highest bit's position compare to n, otherwise 
# 1xxxx & 1xxxx ==1xxxx, so (n | n_r1) need to be 111...1, so 0s has no adjacent 0s.

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n_r1=n>>1
        if (n & n_r1)==0 and (((n | n_r1)+1) & n)==0:
            return True
        else:
            return False
        
