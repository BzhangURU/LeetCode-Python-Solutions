# LC00668_Kth_Smallest_Number_in_Multiplication_Table.py

# Nearly everyone has used the Multiplication Table. The multiplication table of 
# size m x n is an integer matrix mat where mat[i][j] == i * j (1-indexed).

# Given three integers m, n, and k, return the kth smallest element in the m x n 
# multiplication table.

 

# Example 1:


# Input: m = 3, n = 3, k = 5
# Output: 3
# Explanation: The 5th smallest number is 3.
# Example 2:


# Input: m = 2, n = 3, k = 6
# Output: 6
# Explanation: The 6th smallest number is 6.
 

# Constraints:

# 1 <= m, n <= 3 * 10**4
# 1 <= k <= m * n

# Idea: Use binary search, first set multiplication_small=0, multiplication_large=m*n, get each one's total count.
# then binary search to make left+1==right, then find the answer. 


class Solution:
    def getTotalNumbersUnder(self, mul, m, n):
        result=0
        for r in range(1,m+1):
            result+=min(mul//r,n)
        return result
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        mul_small=1
        mul_large=m*n

        if k==1:
            return 1
        elif k==m*n:
            return m*n
        
        while mul_small+1<mul_large:
            mul_middle=(mul_small+mul_large)//2
            middle_count=self.getTotalNumbersUnder(mul_middle,m,n)

            # There is possibility that some mul are prime number larger than max(m,n) that
            # does not contribute to the count_num, so if k==middle_count, maybe the real mul is smaller than mul_middle

            # wrong: if k==middle_count:
            #     return mul_middle
            if k<=middle_count:
                mul_large=mul_middle
            else:
                mul_small=mul_middle
        return mul_large
