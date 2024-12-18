# LC00646_Maximum_Length_of_Pair_Chain_faster.py

# You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.

# A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.

# Return the length longest chain which can be formed.

# You do not need to use up all the given intervals. You can select pairs in any order.

 

# Example 1:

# Input: pairs = [[1,2],[2,3],[3,4]]
# Output: 2
# Explanation: The longest chain is [1,2] -> [3,4].
# Example 2:

# Input: pairs = [[1,2],[7,8],[4,5]]
# Output: 3
# Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].
 

# Constraints:

# n == pairs.length
# 1 <= n <= 1000
# -1000 <= lefti < righti <= 1000

# Idea: sort based on right value, always select min(right), if a pair is not qualified because of left
# value, skip it, then search second min right, third min right.
# change two numbers into one number because left, right is in small range.
# for left or right value, add 1024 to it first
# then right*1024+left as a new number to sort


from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        # for left or right value, add 1024 to it first
        # then right*1024+left as a new number to sort

        list1d=[0]*len(pairs)
        for i in range(len(pairs)):
            list1d[i]=((pairs[i][1]+1024)<<11)+pairs[i][0]+1024

        list1d.sort()
        cur_thresh=list1d[0]>>11#get right value
        result=1

        for i in range(1,len(pairs)):
            # if left value > cur_thresh
            if (list1d[i]&2047)>cur_thresh:
                result+=1
                cur_thresh=list1d[i]>>11
        return result



